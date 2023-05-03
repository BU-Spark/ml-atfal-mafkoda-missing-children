import os
os.chdir('pixel2style2pixel')
from argparse import Namespace
import time
import sys
import pprint
import numpy as np
from PIL import Image
import torch
import torchvision.transforms as transforms
import dlib

sys.path.append(".")
sys.path.append("..")

# from datasets import augmentations
from utils.common import tensor2im, log_input_image
from pixel2style2pixel.models.psp import pSp

#%load_ext autoreload
#%autoreload 2

import cv2
import matplotlib.pyplot as plt 
import dlib
import os.path as osp
import glob
import numpy as np
import Enhancement.RRDBNet_arch as arch
from IPython import display
from tqdm import tqdm
import matplotlib
import tempfile

def run_alignment(image_path):
    from scripts.align_all_parallel import align_face
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    aligned_image = align_face(filepath=image_path, predictor=predictor)
    print("Aligned image has shape: {}".format(aligned_image.size))
    return aligned_image


def run_on_batch(inputs, net, latent_mask=None):
    if latent_mask is None:
        result_batch = net(inputs.to("cuda").float(), randomize_noise=False)
    else:
        result_batch = []
        for image_idx, input_image in enumerate(inputs):
            # get latent vector to inject into our input image
            vec_to_inject = np.random.randn(1, 512).astype('float32')
            _, latent_to_inject = net(torch.from_numpy(vec_to_inject).to("cuda"),
                                      input_code=True,
                                      return_latents=True)
            # get output image with injected style vector
            res = net(input_image.unsqueeze(0).to("cuda").float(),
                      latent_mask=latent_mask,
                      inject_latent=latent_to_inject)
            result_batch.append(res)
        result_batch = torch.cat(result_batch, dim=0)
    return result_batch

#packaging the aligning face into one function
def align_face(img, display=False):
    #setting up model
    experiment_type = 'ffhq_frontalize' 
    EXPERIMENT_DATA_ARGS = {
        "ffhq_frontalize": {
            "model_path": "pixel2style2pixel/pretrained_models/psp_ffhq_frontalization.pt",
            "image_path": "notebooks/images/input_img.jpg",
            "transform": transforms.Compose([
                transforms.Resize((256, 256)),
                transforms.ToTensor(),
                transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])])
        },
    }
    EXPERIMENT_ARGS = EXPERIMENT_DATA_ARGS[experiment_type]
    model_path = EXPERIMENT_ARGS['model_path']
    ckpt = torch.load(model_path, map_location='cpu')
    opts = ckpt['opts']
    pprint.pprint(opts)
    opts['checkpoint_path'] = model_path
    if 'learn_in_w' not in opts:
        opts['learn_in_w'] = False
    if 'output_size' not in opts:
        opts['output_size'] = 1024
    opts = Namespace(**opts)
    net = pSp(opts)
    net.eval()
    net.cuda()
    print('Model successfully loaded!')
    
    #opening image
    original_image = Image.fromarray(img)
    original_image = original_image.convert("RGB")
    original_image.resize((256, 256))
    
    with tempfile.TemporaryDirectory() as tmpdirname:
        cv2.imwrite(os.path.join(tmpdirname, "temp.jpg"),img)
        detector = dlib.get_frontal_face_detector()

        img_test = dlib.load_rgb_image(os.path.join(tmpdirname, "temp.jpg"))
        dets = detector(img_test, 1)

        if len(dets) > 0:
            input_image = run_alignment(os.path.join(tmpdirname, "temp.jpg"))
            input_image.resize((256, 256))
        else:
            input_image = original_image
    
    img_transforms = EXPERIMENT_ARGS['transform']
    transformed_image = img_transforms(input_image)
    
    latent_mask = None
    with torch.no_grad():
        tic = time.time()
        result_image = run_on_batch(transformed_image.unsqueeze(0), net, latent_mask)[0]
        toc = time.time()
        print('Inference took {:.4f} seconds.'.format(toc - tic))
    
    input_vis_image = log_input_image(transformed_image, opts)
    output_image = tensor2im(result_image)
    if display:
        res = np.concatenate([np.array(input_vis_image.resize((256, 256))),
                          np.array(output_image.resize((256, 256)))], axis=1)
    else:
        res = [np.array(output_image.resize((256, 256)))]
    return res 

    
    
    

    