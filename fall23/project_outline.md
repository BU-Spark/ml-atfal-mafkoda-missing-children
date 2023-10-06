# Technical Project Document (v1.0.0-dev, 06 Oct - 2023)

**Authors**: 

- Gitika Jha  
- Sai Surya Varshith Nukala
- Mahaveer Bonagiri 
- Navya Jain

## Overview
Atfal Mafkoda or "missing children" in Arabic, is an organization based in Cairo, Egypt working to reunite missing children, adults, and seniors with their families and loved ones. Initially starting as a Facebook page, it has grown to nearly two million followers and helped over 3,000 missing people. This initiative was also chosen by Facebook as the most influential initiative for the second time in 2020. They are now interested in applying age progression forensics to pictures of the missing children, since some of them have been missing for several years.

## A. Scope of Automation through AI
Here is an overview of the traditional process (without AI):
1. **Posting Missing Persons Information on Facebook**: The photos and known features of missing children and adults are posted on the Facebook page.
2. **Community Engagement**: Members of the community review these posts and message back if they have any information that could help identify the whereabouts of the missing person.
3. **Photo Aging**: Use artists to sketch potential age-progressed images of the missing based on their last available photos.
4. **Verification**: Volunteers visit the location mentioned in the tips and attempt to confirm if the person in question matches the provided photo and features.
5. **Confirmation with Family**: If a match is found, volunteers confirm the identity with the family and gather any extra details or features that can help in the process.

**Challenges with this approach**:
1. It relies too heavily on public memory and tips after sharing images through media channels.
2. Since the appearance changes over time (due to many factors like homelessness or malnutrition), it becomes difficult for humans to identify the missing people accurately.

## B. Problem Statement
1. Generate diverse versions of a face using Generative Adversarial Networks (GANS), integrating factors like homelessness and age into a missing person's image and also incorporate transfer learning to integrate familial facial traits into the generated images for enhanced accuracy.
2. Develop a pipeline for registering these modified faces in a specific format into a database and integrate it with the previous work done.
3. If time permits, we will also explore methods for matching names from the database with Facebook posts using Language Model-based techniques and implement a system for detecting faces within the database.

## C. Checklist for project completion
Here is a list of deliverables expected from us along with our goals for the project:
- **Deliverable 1**: 
  - Team Agreement, Project Outline, Project research document – Within the first 3 weeks of the project
- **Deliverable 2**: 
  - Data preparation and EDA – Weeks 4-5 of the project
- **Deliverable 3**: 
  - Coming up with an improved General Adversarial Network model that produces accurate aged facial images. Add Street Life Effects Filter with effects of malnutrition, sun exposure, and scars to represent harsh living conditions – Weeks 6-9 of the project
- **Deliverable 4**: 
  - Explore lightweight facial recognition models for optimizing and using lower computational resources, ensuring faster processing and compatibility with limited infrastructure – Week 10 of the project
- **Deliverable 5**: 
  - Deployment of the model with the help of client inputs – Week 11 of the project
- **Deliverable 6**: 
  - Final presentation – Week 12

## D. Path to Operationalization
The ultimate goal of this project is to deploy a demo of the model created the way the client wants as a proof of concept. The model we aim to build for generating age-progressed and potentially modified images of missing individuals would take into account factors like homelessness, hunger and aging. Additionally, we plan on storing these modified images into a database for easier facial recognition by the volunteers. Our final end product would be integrating this into the existing tool that the organization has. The final face recognition product should allow users to upload a picture, and then receive a list of results with pictures and other information matched from the database based on the likelihood that the person is the same as the modified pictures of the people in the database. This would improve the pipeline and reduce the time for reuniting the families with the missing people.

## Resources

### Data Sets
- [Fast-AgingGAN](https://github.com/HasnainRaz/Fast-AgingGAN)
- [FaceAgingGAN by ravindrabharathi](https://github.com/ravindrabharathi/FaceAgingGAN)
- [FaceAgingGAN by Gokkulnath](https://github.com/Gokkulnath/FaceAgingGAN)
- [FaceAgingStyleGANs](https://github.com/AbuAbdULLAH-MuhammadAli/FaceAgingStyleGANs)

### References
- https://github.com/yousseb/atfal-ai 
- https://github.com/BU-Spark/ml-atfal-mafkoda-missing-children
- https://github.com/TencentARC/GFPGAN
- https://github.com/BU-Spark/ml-atfal-mafkoda-missing-children 
- https://www.bbc.com/news/world-middle-east-53564935
- https://www.reuters.com/article/us-usa-missing-children/missing-children-in-u-s-nearly-always-make-it-home-alive-idUSBRE83P14020120426
- https://childfindofamerica.org/resources/facts-and-stats-missing-children/
- https://www.insider.com/man-thought-mom-died-reunited-44-years-later-facebook-page-2022-12?fbclid=IwAR0aGF3jHbc7zkusmGX-PgXpDbTP3Dl-AsTsICxBQRjMb4fsfCil6zVz_6g
- https://www.insider.com/man-thought-mom-died-reunited-44-years-later-facebook-page-2022-12?fbclid=IwAR0aGF3jHbc7zkusmGX-PgXpDbTP3Dl-AsTsICxBQRjMb4fsfCil6zVz_6g
- https://www.bbc.com/news/world-middle-east-53564935?fbclid=IwAR0gdikdahzk7Y0QPQejTW2CpAAFTfP41nGgYDqSHodo2IQnuBLcWqNHtpw
- https://restofworld.org/2021/facebook-page-searching-for-egypt-missing-children/
- https://www.theguardian.com/global-development/2022/jan/13/egyptian-media-owner-detained-after-trafficking-and-sexual-assault-claims
- https://english.alarabiya.net/features/2018/02/13/Website-selling-children-based-on-haireye-color-sends-shockwaves-across-Egypt
- https://www.arabnews.com/node/1382181/middle-east


## Weekly Meeting Updates
### 6 Oct 23 - Kickoff meeting
**Attendance**: All students, Youssef, Tom  
**Discussion Points**:
- Introduction to the project
- Starting on Facial Recognition, DB + adding ‘homelessness’ facial features
**Action Items**:
- Go through the required references and come up with material for the project research document
- Think about what the final deployment should look like
- Come up with an updated time for the weekly and bi-weekly meetings
