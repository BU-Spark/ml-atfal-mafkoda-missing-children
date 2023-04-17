import os 
os.environ["SM_FRAMEWORK"] = "tf.keras"
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
os.environ['NUMBAPRO_NVVM']='/share/pkg.7/cuda/11.2/install/nvvm/lib64/libnvvm.so'
os.environ['NUMBAPRO_LIBDEVICE']='/share/pkg.7/cuda/11.2/install/nvvm/libdevice/'
import segmentation_models as sm
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf
import keras
import keras_vggface
from keras_vggface.vggface import VGGFace
import mtcnn
import numpy as np
import matplotlib as mpl
from keras.utils.data_utils import get_file
import dlib
import keras_vggface.utils
import PIL
import os.path
os.environ['KMP_DUPLICATE_LIB_OK']='True'
from deepface import DeepFace
import pandas as pd
import sys

models = [
  "VGG-Face", 
  "Facenet", 
  "Facenet512", 
  "OpenFace", 
  "DeepFace", 
  "DeepID", 
  "ArcFace", 
  "Dlib", 
  "SFace",
]

def db_find(path, db, model=0, thresh):
    m = model
    dfs = DeepFace.find(img_path=path, db_path=db, model_name=models[m],
                        detector_backend="mtcnn", enforce_detection=False)
    df = dfs[0].copy()
    df['id'] = df['identity'].str.strip("atfalmafkoda_unzip/database/person").str.split("/")
    df['id'] = df['id'].apply(lambda x: x[0])
    imgs = df.loc[df["VGG-Face_cosine"] < .25]
    return imgs

def main(arg1, arg2):
    imgs = db_find(arg1, arg2)
    return imgs['identity']
    
if __name__ == "__main__":
    args = sys.argv[1:]
    arg1 = args[0]
    arg2 = args[1]

    main(arg1, arg2)
