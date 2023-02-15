# Atfal Mafkoda ("Missing Children") Project Description

## Matthew Batacan, Ryan Nie, William Lee, Daniel Skahill  2022-02-14 v1.0.0-dev_


## Overview

*Atfal Mafkoda*, or "missing children" in Arabic, is an organization based in Cairo, Egypt working to reunite missing children, adults, and seniors with their families and loved ones. Rami El-Gebali founded Atfal Mafkoda in 2016 after realizing that there was no formal infrastructure for locating missing persons. He started a Facebook page that relatives and loved ones of missing people could contact for help. Initially serving and reuniting dozens of families, Atfal Mafkoda has grown substantially and is in the process of helping locate thousands of missing persons with nearly two million followers.

Children may be kidnapped or trafficked for a variety of reasons including organ trade, sex work, adoption, begging, ransom, or they may just runaway. While Atfal Mafkoda has already helped find and reunite over 3000 missing people, they are now facing the difficulty of locating people who have been lost for an extended period of time because their appearances may have significantly changed. 

Atfal Mafkoda has come to BU Spark! with the proposal of developing software that could generate new photographs of missing persons that could reflect their current age and the environment they may be living in. In addition, Atfal Mafkoda would like to explore face recognition and potentially utilize this technology to help identify people who come to orphanages, hospitals, or other safe havens. 

The aging software may be constructed using General Adversarial Networks along with style transfer networks, and the recognition software may be constructed using deep convolutional neural networks. Other methods will be explored, however, these are the ones that currently seem to be the most promising. 

Even if the software developed leads to just one more missing person reunited with their loved ones, the project will be a success-- if it proves to be a valuable asset and leads to more than one missing person found, the technology can potentially be utilized in broader contexts across the world (i.e. the US government has expressed some interest). Regardless, everything developed will be open source so that individual contributers can help strengthen the project. 

### A. Problem Statement: 

There are <insert_statistics> children that went missing from <insert_years> to <insert_years>, and it can be incredibly difficult for volunteers to find these missing children after several years. Children grow up fast, and their facial structures can change drastically in the span of a few years depending on their status (homelessness, scars, hunger, etc.).

To facilitate the search for missing people, our team is developing a face ageing software using state-of-the-art machine learning algorithms. Hopefully, with new images that reflect the current ages and conditions of missing people, our volunteers can help reunite the missing people with their families faster.


### B. Checklist for project completion

_Provide a bulleted list of the concrete deliverables and artifacts that, when complete, define the completion of the
 project._



1. Improved forensic face aging GAN
2. Transferring facial features of family members to face aged photos
3. Simulating the visual effects of homlessness, or other confounding factors on face aged photos.
4. Face matching/recognition algorithm to narrow the lsit of possible matches to a candidate.


### C. Provide a solution in terms of human actions to confirm if the task is within the scope of automation through AI. 

_To assist in outlining the steps needed to achieve our final goal, outline the AI-less process that we are trying to 
automate with Machine Learning. Provide as much detail as possible._

When dealing with missing children in the United States around 98% of cases are solved with the aid from local law enforcement agencies. You can ask investigators enter your child into the National Crime Information Center. Investigators then take recent photographs of the missing child, along with contact information of anyone that would have information on the childs whereabouts. From this law enforcement investigators take the information along with contacts and databases to cross-reference to find the child. 

### D. Outline a path to operationalization.

_Data Science Projects should have an operationalized end point in mind from the onset. Briefly describe how you see the tool
 produced by this project being used by the end user beyond a jupyter notebook or proof of concept. If possible, be specific and
 call out the relevant technologies_

END RESULT - Demo on huggingface

## Resources


### Data Sets


*  To be provided by clients.


### References



1. [Atfal Mafkoda Website](https://atfalmafkoda.com/en/home)

2. [Original Research Paper on GANs](https://arxiv.org/abs/1406.2661)

3. [Paper on CycleGANs](https://arxiv.org/abs/1703.10593)


4 tasks, 3 are GAN based/style transfer, 1 is race recognition
- get data asap
- recognition- embedding vector; distance measures from the embedding vectors
- it's possible the recognizer could still have a good similarity
- using existing gans to see which are most robust
- relatives
- style transfer 
- difusion models?