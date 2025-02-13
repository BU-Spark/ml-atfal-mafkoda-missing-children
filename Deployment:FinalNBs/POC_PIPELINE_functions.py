# In order to run the code, you need to clone into your root director:
# - https://github.com/eladrich/pixel2style2pixel
# - https://github.com/AbuAbdULLAH-MuhammadAli/FaceAgingStyleGANs
# 
# From https://github.com/davisking/dlib-models download the models (you may have to change the paths in the code):
# - mmod_human_face_detector.dat (use to detect face)
# - shape_predictor_68_face_landmarks.dat (use to detect face)
# 
# From https://drive.google.com/file/d/1pJ_T-V1dpb1ewoEra1TGSWl5e6H7M4NN/view download:
# - RRDB_ESRGAN_x4.pth  (use to enhance image)

import os
# change to directory to pixel2style2pixel
# insert where you have this directory located
os.chdir('../pixel2style2pixel')

from argparse import Namespace
import time
import sys
import pprint
import numpy as np
from PIL import Image
import torch
import torchvision.transforms as transforms
import dlib
import tempfile

sys.path.append(".")
sys.path.append("..")

# from datasets import augmentations
from utils.common import tensor2im, log_input_image
from pixel2style2pixel.models.psp import pSp

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


# 1. Crop Faces with Bounding Box 

face_detector_path = cnn_model_path = '/projectnb/sparkgrp/ml-atfal-mafkoda-grp//dlib_model/mmod_human_face_detector.dat' #change for your path
cnn_face_detector = dlib.cnn_face_detection_model_v1(face_detector_path)

def detect_crop_face(img, display=False):
    output_image = img.copy()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = cnn_face_detector(imgRGB,upsample_num_times =2)
    
    for bbox in results:
        x1 = bbox.rect.left()
        y1 = bbox.rect.top()
        x2 = bbox.rect.right()
        y2 = bbox.rect.bottom()
        w = x2-x1
        h = y2-y1
        
        x_adj = int(0.5*w )
        y_adj = int(0.5*h)
        x1_adj = x1-x_adj
        y1_adj = y1-y_adj
        x2_adj = x2+x_adj
        y2_adj = y2+y_adj
        points_adjust =[x1_adj,y1_adj,x2_adj,y2_adj]
        
        if x1_adj < 0:
            x1_adj = 0
        if y1_adj < 0:
            y1_adj = 0
        
        output_image = output_image[y1_adj:y2_adj,x1_adj:x2_adj]
    if display:
        plt.imshow(cv2.cvtColor(output_image,cv2.COLOR_BGR2RGB))
        plt.show()
    return output_image

# 2. Enhance Faces

def enhance_face(img):
    model_path = '/projectnb/sparkgrp/ml-atfal-mafkoda-grp/Enhancement/models/RRDB_ESRGAN_x4.pth' # load the model
    device = torch.device('cuda')  # if you want to run on CPU, change 'cuda' -> cpu
    # device = torch.device('cpu')

    model = arch.RRDBNet(3, 3, 64, 23, gc=32)
    model.load_state_dict(torch.load(model_path), strict=True)
    model.eval()
    model = model.to(device)

    output = None
    img = img * 1.0 / 255
    img = torch.from_numpy(np.transpose(img[:, :, [2, 1, 0]], (2, 0, 1))).float()
    img_LR = img.unsqueeze(0)
    img_LR = img_LR.to(device)

    with torch.no_grad():
        output = model(img_LR).data.squeeze().float().cpu().clamp_(0, 1).numpy()
    output = np.transpose(output[[2, 1, 0], :, :], (1, 2, 0))
    output = (output * 255.0).round()
#     cv2.imwrite('Enhancement/results/{:s}_rlt.png'.format(base), output)
    return output



# 3. Align Faces

experiment_type = 'ffhq_frontalize' 
EXPERIMENT_DATA_ARGS = {
    "ffhq_frontalize": {
        "model_path": "/projectnb/sparkgrp/ml-atfal-mafkoda-grp/pixel2style2pixel/pretrained/psp_ffhq_frontalization.pt",
        "image_path": "/projectnb/sparkgrp/ml-atfal-mafkoda-grp/pixel2style2pixel/notebooks/images/input_img.jpg",
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


#next two functions are helper functions defined by psp notebook
def run_alignment(image_path):
    from scripts.align_all_parallel import align_face
    predictor = dlib.shape_predictor("/projectnb/sparkgrp/ml-atfal-mafkoda-grp/shape_predictor_68_face_landmarks.dat")
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
def align_face(img, net, display=True):
    original_image = Image.open(img)
    original_image = original_image.convert("RGB")
    original_image.resize((256, 256))
    
    input_image = run_alignment(img)
    input_image.resize((256, 256))
    
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
        res = np.concatenate([np.array(output_image.resize((256, 256)))], axis=1)
    res_image = Image.fromarray(res)
    return res_image
    
# ## 4. Pass through FaceAgingGAN
os.chdir('/projectnb/sparkgrp/ml-atfal-mafkoda-grp/FaceAgingStyleGANs')
from collections import OrderedDict
from options.test_options import TestOptions
from data.data_loader import CreateDataLoader
from FaceAgingStyleGANs.models.models import create_model
import util.util as util
from util.visualizer import Visualizer

opt = TestOptions().parse(save=False)
opt.display_id = 0 # do not launch visdom
opt.nThreads = 1   # test code only supports nThreads = 1
opt.batchSize = 1  # test code only supports batchSize = 1
opt.serial_batches = True  # no shuffle
opt.no_flip = True  # no flip
opt.in_the_wild = True # This triggers preprocessing of in the wild images in the dataloader
opt.traverse = True # This tells the model to traverse the latent space between anchor classes
#opt.interp_step = 0.05 # this controls the number of images to interpolate between anchor classes


#wrapper function for aging the face
def age_face(img, opt, gender, d):
    os.chdir('/projectnb/sparkgrp/ml-atfal-mafkoda-grp/FaceAgingStyleGANs')
    data_loader = CreateDataLoader(opt)
    dataset = data_loader.load_data()
    visualizer = Visualizer(opt)
    
    if gender == 'male':
        opt.name = 'males_model'
    else: 
        opt.name = 'females_model' 
    
    model = create_model(opt)
    model.eval()
    
    data = dataset.dataset.get_item_from_path(img)
    visuals = model.inference(data)
    
    os.makedirs('results', exist_ok=True)
    out_path = '/projectnb/sparkgrp/ml-atfal-mafkoda-grp/model_deployment/results/output' 
    #print(out_path)
    visualizer.save_images_deploy(visuals, out_path)
    #visualizer.save_row_image(visuals, out_path, traverse=True)
    out_dir = out_path.strip('output')
    return out_dir

import gc

def inference(img, gender='male', detect=True, enhance=True, align=True):

    os.chdir('/projectnb/sparkgrp/ml-atfal-mafkoda-grp/')
    img_path = '/projectnb/sparkgrp/ml-atfal-mafkoda-grp/model_deployment/results/inference.jpeg'
    cv2.imwrite(img_path,img)
    
    img_load = cv2.imread(img_path)
    img_load = cv2.cvtColor(img_load,cv2.COLOR_BGR2RGB)
    
    if detect:
        img = detect_crop_face(img_load)
    if enhance:
        img = enhance_face(img)
    img = img.astype(np.uint8)
    with tempfile.TemporaryDirectory() as tmpdirname:
        print('created temporary directory', tmpdirname)
        if align:
            cv2.imwrite(os.path.join(tmpdirname, os.path.basename(img_path)),img)
            img = align_face(os.path.join(tmpdirname, os.path.basename(img_path)), net, display=False)
            img.save(os.path.join(tmpdirname, os.path.basename(img_path)), "JPEG") 
        else:
            cv2.imwrite(os.path.join(tmpdirname, os.path.basename(img_path)),img)
        
        out = age_face(os.path.join(tmpdirname, os.path.basename(img_path)), opt, gender, tmpdirname)

    os.chdir('/projectnb/sparkgrp/ml-atfal-mafkoda-grp/model_deployment/results/')
    
    os.rename('output_tex_trans_to_class_0.png','output_tex_trans_to_class_00.png')
    os.rename('output_tex_trans_to_class_1.png','output_tex_trans_to_class_01.png')
    os.rename('output_tex_trans_to_class_2.png','output_tex_trans_to_class_02.png')
    os.rename('output_tex_trans_to_class_3.png','output_tex_trans_to_class_03.png')
    os.rename('output_tex_trans_to_class_4.png','output_tex_trans_to_class_04.png')
    os.rename('output_tex_trans_to_class_5.png','output_tex_trans_to_class_05.png')
    os.rename('output_tex_trans_to_class_6.png','output_tex_trans_to_class_06.png')
    os.rename('output_tex_trans_to_class_7.png','output_tex_trans_to_class_07.png')
    os.rename('output_tex_trans_to_class_8.png','output_tex_trans_to_class_08.png')
    os.rename('output_tex_trans_to_class_9.png','output_tex_trans_to_class_09.png')
    #os.rename('output_tex_trans_to_class_10.png')
    
    out_list = os.listdir()
    out_list.remove('flagged')
    out_list.remove('gradio_cached_examples')
    out_list.remove('inference.jpeg')
    out_list.remove('output_orig_img.png')
    out_list.remove('.ipynb_checkpoints')
    print(sorted(out_list))    
    return sorted(out_list)


# Args for inference
# - img: image path
# - opt: optimizer for face aging GAN (defined above, just pass in "opt")
# - gender: target gender for face 
# - detect: boolean T/F- set to True if you want to detect the face
# - enhance: boolean T/F- set to True if you want to enhance the image (not recommended for good quality images)
# - align: boolean T/F- set to True if the face is not frontalized (not recommended if face is already frontalized)
