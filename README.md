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

5. Download the "Atfal Mafkoda Missing People" database from https://drive.google.com/file/d/1252bZG0sUNZ_eJZlZKTobUmOLeV9G-nM/view?usp=share_link

*if running from the BU SCC, ensure that the modules python 3.8.10, cuda 11.3, and gcc 9.3.0 are loaded prior to running interactive sessions.
*please ensure you allocate at least one GPU before running any of the code.








### Known Issues:
1. There is a current issue after importing keras_vggface. You will need to make the change:

`from keras.engine.topology import get_source_inputs`

to

`from keras.utils.layer_utils import get_source_inputs` in `keras_vggface/models.py`.
