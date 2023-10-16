# Research Phase

## Relevant Papers

### **Face Aging with Conditional Generative Adversarial Networks (Antipov et al. 2017)**
[Link to paper](https://arxiv.org/pdf/1702.01983.pdf)

- **Summary:**
    - The authors present a method for automatically aging faces while preserving the original person's identity (identity-preserving) using a Generative Adversarial Network (GAN) called Age Conditional Generative Adversarial Network (Age-cGAN).
    - Age-cGAN, a GAN designed to generate high-quality synthetic images within specific age categories - is introduced in this paper.
    - They propose a novel latent vector optimization approach that preserves the original person's identity during face aging.
    - **Two-Step Face Aging Process:** 
        1. Reconstructing an input face image using an optimal latent vector that preserves the original identity.
        2. Generating the final aged face image by changing the age condition using the preserved identity.
    - The paper explains how face reconstruction is performed using Age-cGAN and discusses the need for latent vector optimization.

### **FaceShifter: Towards High Fidelity And Occlusion Aware Face Swapping (Li et al. 2020)**
[Link to paper](https://arxiv.org/abs/1912.13457)

- **Summary:**
    - This paper introduces a novel approach for face swapping using a two-stage framework that aims to generate high-quality and realistic face swaps while addressing facial occlusions.
    - **Methodology:**
        1. In the first stage, the framework leverages the target image's attributes to synthesize a high-fidelity swapped face.
        2. Further, to address the challenges of facial occlusions, the second stage introduces a Heuristic Error Acknowledging Refinement Network (HEAR-Net).
    - The results demonstrate that the outcomes are not only visually appealing but also excel in preserving the subject's identity. Moreover, this approach is capable of generating realistic face images without subject-specific training, which will be very useful for our project.


### **Face Aging with Identity-Preserved Conditional Generative Adversarial Networks**
[Link to paper](https://ieeexplore.ieee.org/document/8578926)

- **Summary:**
    - The paper proposes an Identity-Preserved Conditional Generative Adversarial Networks (IPCGANs) framework for face aging, which aims to synthesize a face with a target age while preserving the identity of the input face.
    - This paper tries to produce the face with specific age groups rather than a particular age and claims to be better than (Antipov et al. 2017) as mentioned above, we are aiming to check whether it is true and apply it to current pipeline to improve the face aging.



## Data Requirements
We request the following data:

- Photos of currently missing children
- Photos of recovered children and their original missing child photo
- Photos of family members from both #1 and #2.
- Gender and the age (or date of birth) of the person who went missing.

## Existing Datasets

- [IMDb-Wiki Dataset](https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/) - this dataset can be used to train the face-aging conditional GAN 

- [KinFaceW Dataset](https://www.kinfacew.com/download.html) –  this dataset can be used for kinship recognition

- [FIW Dataset](https://web.northeastern.edu/smilelab/fiw/) –this dataset can also be used for kinship recognition. Both of these datasets will help in the training for the ‘family-morphing’ part


## ML Approach and Reasoning 

1. Using optimal latent vector (identity-preserving) to create a CGAN for face aging.
2. Applying high-quality and realistic face swaps using the methodology in ‘FaceShifter’ to apply more filters during matching – contributing to both the ‘homelessness’ factor as well as the ‘family morphing’ factor of the project.
3. We have attempted to reference pertinent papers for the homelessness feature; however, none of the sources appear to yield satisfactory results. Furthermore, the requisite dataset is currently unavailable. We will engage in a discussion with the client to determine the most appropriate course of action moving forward.

## Performance Criteria

- Utilizing the training set with images of missing children and their current photographs for performance assessment against the test set.
- Emphasizing meticulous data selection and preparation after client discussions.
- Employing evaluation metrics post-training, with a specific emphasis on accuracy.
- Ensuring the preservation of subject identity, especially in the context of the 'FaceShifter' methodology.
- Prioritizing cost-effectiveness and high efficiency in both the model and system.



