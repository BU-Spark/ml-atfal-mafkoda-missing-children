# About the Notebooks


`AgeDBImages.ipynb` is similar to POC pipeline, but contains code that will input aged faces and frontalized faces into the database. 
- If using a new database, we recommend running this first.

`Facial-Recognition-Demo.ipynb` and `DeepFace-FR-Testing.ipynb` supersede `DeepFace FR Beta Deployment.ipynb`
- In `Facial-Recognition-Demo.ipynb` notebook you will find how to run the Gradio interface.
- In `DeepFace-FR-Testing.ipynb` you will see how we tested the facial recognition capabilities (if you would like the testing databases which are different form the main database, please contact us).
- Please download the database [here](https://drive.google.com/file/d/1252bZG0sUNZ_eJZlZKTobUmOLeV9G-nM/view?usp=share_link) (embedding vectors are already present in this database, so it should take less than a few minutes to run).

`face_aging_app.ipynb` is the Gradio interface for simply aging faces.

`align.py` is simply a helper script for frontalization in the Gradio Demo.


## Notes
* In order to run the notebooks, you must have available GPUs. 
* Some paths may need to be changed.
