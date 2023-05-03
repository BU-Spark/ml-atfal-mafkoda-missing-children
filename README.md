# Documentation 

## Steps to reproduce code
1. `git clone https://github.com/BU-Spark/ml-atfal-mafkoda-missing-children.git`
2. Create and/or activate a new virtual environment with `python3.8.10`, then use `pip install -r requirements.txt` to install the dependencies.
3. `git clone`:

- [pixel2style2pixel](https://github.com/eladrich/pixel2style2pixel)
- [FaceAgingStyleGANs](https://github.com/AbuAbdULLAH-MuhammadAli/FaceAgingStyleGANs)

4. From [dlib-models](https://github.com/davisking/dlib-models) download the models (you may have to change the paths in the code):

- mmod_human_face_detector.dat (used to detect face)
- shape_predictor_68_face_landmarks.dat (used to detect face)

5. From [this Google Drive](https://drive.google.com/file/d/1pJ_T-V1dpb1ewoEra1TGSWl5e6H7M4NN/view) download:

- RRDB_ESRGAN_x4.pth (use to enhance image)

6. Download the "Atfal Mafkoda Missing People" database [here](https://drive.google.com/file/d/1252bZG0sUNZ_eJZlZKTobUmOLeV9G-nM/view?usp=share_link).

## Deployment
- The deployment codes are inside Deployment:FinalNBs folder
- You can run the face aging gradio app in face_aging_app.ipynb
- You can run the face recognition gradio app in DeepFace FR Beta Deployment.ipynb

## SCC Notes
* If running from the BU SCC, ensure that the modules **python 3.8.10, cuda 11.3, and gcc 9.3.0** are loaded prior to running interactive sessions.
* Please ensure you allocate at least one GPU before running any of the code (**3.5 K40m or P100 or V100** is ok, but certain GPUs (K40m) might not work. In that case wait until the other GPUs are free, then restart the SCC interactive session).

### Roadmap of Repository Directories
- [`DeploymentFinalNBs`](https://github.com/BU-Spark/ml-atfal-mafkoda-missing-children/tree/dev/Deployment:FinalNBs)- contains the deployment notebooks for the face aging demo as well as the facial recognition demo
- [`POC`](https://github.com/BU-Spark/ml-atfal-mafkoda-missing-children/tree/dev/POC)- contains the files for our proof of concept pipeline
- [`data-EDA`](https://github.com/BU-Spark/ml-atfal-mafkoda-missing-children/tree/dev/data-EDA)- contains notebooks for our exploratory data analysis
- [`database`](https://github.com/BU-Spark/ml-atfal-mafkoda-missing-children/tree/dev/database)- contains non-aged and non-frontalized photos for missing people; the version with aged and frontalized photos can be found in the link above
- [`results`](https://github.com/BU-Spark/ml-atfal-mafkoda-missing-children/tree/dev/results)- test image results from our POC pipeline runs; shows faces of missing people and the aged/frontalized outputs


## Known Issues
1. There is a current issue after importing keras_vggface. You will need to make the change:

`from keras.engine.topology import get_source_inputs`

to

`from keras.utils.layer_utils import get_source_inputs` in `keras_vggface/models.py`.

2. When running the Facial Recognition notebook, a pickle file will be created with the embedding vectors of each image after running the FR once. This should take a little over an hour to do. If new images are added, you must delete the pickle file and rerun the FR notebook to create new embeddings, there is currently no way to append the pickle file with the new embeddings. 

## Citations 
PSP
```
@InProceedings{richardson2021encoding,
      author = {Richardson, Elad and Alaluf, Yuval and Patashnik, Or and Nitzan, Yotam and Azar, Yaniv and Shapiro, Stav and Cohen-Or, Daniel},
      title = {Encoding in Style: a StyleGAN Encoder for Image-to-Image Translation},
      booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
      month = {June},
      year = {2021}
}
```

FaceAgingGAN
```
@inproceedings{orel2020lifespan,
  title={Lifespan Age Transformation Synthesis},
  author={Or-El, Roy
          and Sengupta, Soumyadip
          and Fried, Ohad
          and Shechtman, Eli
          and Kemelmacher-Shlizerman, Ira},
  booktitle={Proceedings of the European Conference on Computer Vision (ECCV)},
  year={2020}
}
```



