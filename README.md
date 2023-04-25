# Documentation 

### Steps to reproduce code
1. `pip install -r requirements.txt` in a new virtual environment
2. `git clone`:

- https://github.com/eladrich/pixel2style2pixel
- https://github.com/AbuAbdULLAH-MuhammadAli/FaceAgingStyleGANs

3. From https://github.com/davisking/dlib-models download the models (you may have to change the paths in the code):

- mmod_human_face_detector.dat (use to detect face)
- shape_predictor_68_face_landmarks.dat (use to detect face)

4. From https://drive.google.com/file/d/1pJ_T-V1dpb1ewoEra1TGSWl5e6H7M4NN/view download:

- RRDB_ESRGAN_x4.pth (use to enhance image)







### Known Issues:
1. There is a current issue after importing keras_vggface. You will need to make the change:

`from keras.engine.topology import get_source_inputs`

to

`from keras.utils.layer_utils import get_source_inputs` in `keras_vggface/models.py`.
