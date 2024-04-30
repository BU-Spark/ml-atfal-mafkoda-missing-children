# Documentation 


## Roadmap of Repository Directories
- [`DeploymentFinalNBs`](https://github.com/BU-Spark/ml-atfal-mafkoda-missing-children/blob/dev/spring24/Final_Deployment_Spring_2024.ipynb) - contains the deployment notebook for applying homelessness and parsing
- [`POC`](https://github.com/BU-Spark/ml-atfal-mafkoda-missing-children/blob/dev/spring24/POC_Spring_24.ipynb) - contains the files for our proof of concept pipeline
- [`data-EDA`](https://github.com/BU-Spark/ml-atfal-mafkoda-missing-children/blob/dev/spring24/EDA_Spring_24.ipynb) - contains notebooks for our exploratory data analysis
- [`database`](https://github.com/BU-Spark/ml-atfal-mafkoda-missing-children/tree/dev/database) - contains non-aged and non-frontalized photos for missing people; the version with aged and frontalized photos can be found in the link above
- [`results`](https://github.com/BU-Spark/ml-atfal-mafkoda-missing-children/tree/dev/results) - test image results from our POC pipeline runs; shows faces of missing people and the aged/frontalized outputs


## Steps to reproduce code
1. `git clone https://github.com/BU-Spark/ml-atfal-mafkoda-missing-children.git`

2. Follow instructions given in the final deployment notebook (given in the first block). [https://github.com/BU-Spark/ml-atfal-mafkoda-missing-children/blob/dev/spring24/Final_Deployment_Spring_2024.ipynb]

## Deployment
- Run the code in the final deployment file placed in spring24 folder in sequential order while carefully reading through instructions.


## SCC Notes
* If running from the BU SCC, ensure that the modules spring-2024-pyt and swap-auto-pytorch are able to be loaded from the current session.
* Please ensure you allocate at least one GPU before running any of the code (**3.5 K40m or P100 or V100** is ok, but certain GPUs (K40m) might not work. In that case wait until the other GPUs are free, then restart the SCC interactive session).


## Known Issues
1. The DeepFace conda environment is incompatible with the Swapping AutoEncoder model. Ensure to swap to the appropriate environments for each model and to load the proper variables regarding directories and imports after swapping environments.


## Citations 
DeepFace
```
@INPROCEEDINGS{6909616,
  author={Taigman, Yaniv and Yang, Ming and Ranzato, Marc'Aurelio and Wolf, Lior},
  booktitle={2014 IEEE Conference on Computer Vision and Pattern Recognition}, 
  title={DeepFace: Closing the Gap to Human-Level Performance in Face Verification}, 
  year={2014},
  volume={},
  number={},
  pages={1701-1708},
  keywords={Face;Three-dimensional displays;Training;Face recognition;Agriculture;Solid modeling;Shape},
  doi={10.1109/CVPR.2014.220}}
```

Swapping Autoencoder for Deep Face Manipulation
```
@misc{park2020swapping,
      title={Swapping Autoencoder for Deep Image Manipulation}, 
      author={Taesung Park and Jun-Yan Zhu and Oliver Wang and Jingwan Lu and Eli Shechtman and Alexei A. Efros and Richard Zhang},
      year={2020},
      eprint={2007.00653},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```



