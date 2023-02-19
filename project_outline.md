# Atfal Mafkoda ("Missing Children") Project Description

## Matthew Batacan, Ryan Nie, William Lee, Daniel Skahill  2022-02-14 v1.0.0-dev_


## Overview

*Atfal Mafkoda*, or "missing children" in Arabic, is an organization based in Cairo, Egypt working to reunite missing children, adults, and seniors with their families and loved ones. Rami El-Gebali founded Atfal Mafkoda in 2016 after realizing that there was no formal infrastructure for locating missing persons. He started a Facebook page that relatives and loved ones of missing people could contact for help. Initially serving and reuniting dozens of families, Atfal Mafkoda has grown substantially and is in the process of helping locate thousands of missing persons with nearly two million followers.

Children may be kidnapped or trafficked for a variety of reasons including organ trade, sex work, adoption, begging, ransom, or they may just runaway. While Atfal Mafkoda has already helped find and reunite over 3000 missing people, they are now facing the difficulty of locating people who have been lost for an extended period of time because their appearances may have significantly changed. 

Atfal Mafkoda has come to BU Spark! with the proposal of developing software that could generate new photographs of missing persons that could reflect their current age and the environment they may be living in. In addition, Atfal Mafkoda would like to explore face recognition and potentially utilize this technology to help identify people who come to orphanages, hospitals, or other safe havens. 

The aging software may be constructed using General Adversarial Networks along with style transfer networks, and the recognition software may be constructed using deep convolutional neural networks. Other methods will be explored, however, these are the ones that currently seem to be the most promising. 

Even if the software developed leads to just one more missing person reunited with their loved ones, the project will be a success-- if it proves to be a valuable asset and leads to more than one missing person found, the technology can potentially be utilized in broader contexts across the world (i.e. the US government has expressed some interest). Regardless, everything developed will be open source so that individual contributers can help strengthen the project. 

### A. Problem Statement: 

Children grow up fast, and their facial structures can change drastically in the span of a few years depending on their status (homelessness, scars, hunger, etc.). Therefore, after a child has been missing for several years, it is extremely difficult to locate them without an accurate representation of what they may look like today.

To facilitate the search for missing people, our team is developing a face ageing software using state-of-the-art machine learning algorithms. Hopefully, with new images that reflect the current ages and conditions of missing people, our volunteers can help reunite the missing people with their families faster.

In addition, our team will develop a facial recognition system that can help orphanages, hospitals, and safe havens identify potential missing children when they are admitted. 


### B. Checklist for project completion

1. Team Agreement
2. Research Document
3. Midterm Presentation
4. Improved forensic face aging GAN
* When: before final presentation
* Definition: use GAN model to generate aged faces, achieve high similarity compared with recovered children's faces
5. Transferring facial features of family members to face aged photos
* When: 1 month after midterm presentation
* Definitno: transfer relatives' facial features to missing children's images, increase similarity compared with relatives' images
6. Simulating the visual effects of homlessness, or other confounding factors on face aged photos.
* When: 2 months after midterm presentation
* Defintion: Add visual reflect that would mimic the situation of homeless
7. Face matching/recognition algorithm to narrow the lsit of possible matches to a candidate.
* When: before midterm presentation
* Definition: Without generating new faces, use matching/recognition algorithm to find a set of similar faces with high similarities
8. Image Enhancement
* When: before final presentation
* Definition: increase the image resolution, obtaining larger matrice as inputs
9. Final Presentation/Demo

### C. Provide a solution in terms of human actions to confirm if the task is within the scope of automation through AI. 

When dealing with missing children in the United States around 98% of cases are solved with the aid from local law enforcement agencies. You can ask investigators to enter your child into the National Crime Information Center. Investigators then take recent photographs of the missing child, along with contact information of anyone that would have information on the childs whereabouts. From this, law enforcement investigators take the information and use contacts and databases to cross-reference sources to find the child. 

Essentially, the AI portion of this project will enable volunteers to quickly age and style faces of missing children so that they can post them to the Atfal Mafkoda Facebook group in hopes that someone has seen the missing person who looks similar to the aged version. In terms of facial recogntion, this AI technology would allow anyone to quickly upload an image of someone who they think may be a victim of abduction to see if their face matches anyone in the database (this would be impossible to do manually). 

### D. Outline a path to operationalization.
 
By the end of the semester, we will present a demo of our models using Huggingface. This will essentially serve as the proof of concept, but it will not be the final product. The final face-aging product should be operational software (such as a web application) that allows users to upload a photo, age the photo according to specified input (desired age, living conditions, hair length, etc.) and then output a rendering of the generated image. The final face recognition product should allow users to upload a photo, and then receive a list of results (photos, names, and relevant information) back based on the likelihood that the person uploaded is the same in the images returned. 

## Resources

1. [Original Research Paper on GANs](https://arxiv.org/abs/1406.2661)

2. [Paper on CycleGANs](https://arxiv.org/abs/1703.10593)

3. [GAN Project Similar to Desired Output](https://github.com/AbuAbdULLAH-MuhammadAli/FaceAgingStyleGANs)

### Data Sets

1. Data provided by Atfal Mafkoda

2. [FGNET](https://www.v7labs.com/open-datasets/fg-net#:~:text=FGNet%20is%20a%20dataset%20for,gap%20up%20to%2045%20years)

3. [MORPH](https://uncw.edu/oic/tech/morph.html)

4. [CACD](https://www.v7labs.com/open-datasets/cacd)

5. [AgeDB](https://www.kaggle.com/nitingandhi/agedb-database)

6. ITWCC

7. [LFITW](http://vis-www.cs.umass.edu/lfw/)

### References

1. [Atfal Mafkoda Website](https://atfalmafkoda.com/en/home)
