# Documentation 

### Steps to reproduce code
1. `pip install -r requirements.txt` in a new virtual environment
2. download github dependencies listed in POC notebook into the root folder







### Known Issues:
1. There is a current issue after importing keras_vggface. You will need to make the change:

`from keras.engine.topology import get_source_inputs`

to

`from keras.utils.layer_utils import get_source_inputs` in `keras_vggface/models.py`.
