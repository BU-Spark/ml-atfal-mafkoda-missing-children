**Research**



1. Latent Vectors and Identity Preservation
    - Face Aging with Conditional Generative Adversarial Networks: [https://arxiv.org/pdf/1702.01983.pdf](https://arxiv.org/pdf/1702.01983.pdf)
        - Age-cGAN (see image on paper for structure)
        - cGANs allow for more flexible input (i.e. can input different ages whereas GANs only allow one type of input)
        - Essentially what we want to do is have an input vector x with age y and remap x to y’. Currently x can be represented as x = G(z, y) where z is the ground truth vector, and y is the age. We need to find a latent vector z* such that x ~ G(z*, y) then we can use z* and y’ to achieve x’.
        - Identity preserving latent vector can be generated using a facial recognition network
            - “given a face recognition neural network FR able to recognize a person’s identity in an input face image x, the difference between the identities in the original and reconstructed images x and ¯x can be expressed as the Euclidean distance between the corresponding embeddings FR(x) and FR(¯x). Hence, minimizing this distance should improve the identity preservation in the reconstructed image ¯x”
        - **OpenFace** is open source facial recognition software (might be very helpful for facial recognition task or for identity preserving latent vectors)
2. GANs
    - Lifespan Age Transformation: [https://arxiv.org/pdf/2003.09764.pdf](https://arxiv.org/pdf/2003.09764.pdf)
        - Used 6 classes for age ranges based on age theory (look into this more); age development is nonlinear 
        - Algorithm aimed to 
            - Learn the head shape
            - Learn appearance changes across different ages
        - Ideally would have used supervised learning, but requires large amount data that isn’t currently available
        - GAN has 1 conditional generator (ages) and 1 discriminator
        - Conditional generator (similar to StyleGAN2)
            - Identity encoder- age and identity encoded separately because identity is constant
            - Mapping network
            - Decoder
        - Discriminator is StyleGAN
        - Used FFHQ-Aging dataset
        - *LATS model works surprisingly well with it’s demo.
3. Alternatives to GANs
    - Face Aging with GAN: [https://cs230.stanford.edu/projects_fall_2019/reports/26262064.pdf](https://cs230.stanford.edu/projects_fall_2019/reports/26262064.pdf)
        - Prototyping- taking lots of images from a specific age group and creating an average face; then apply style transfer to other faces
        - Modeling based- tracks key features over time and recognizes differences from latent vector (this is very time consuming)
    - [https://arxiv.org/pdf/2012.03459.pdf](https://arxiv.org/pdf/2012.03459.pdf) (Github: [https://github.com/Hzzone/PFA-GAN](https://github.com/Hzzone/PFA-GAN))
        - The existing conditional generative adversarial networks (cGANs) typically use a single network to learn various aging effects between any two different age groups. 
        - This paper proposes a novel progressive face aging framework based on generative adversarial network (PFA-GAN), this network contains several sub-networks to mimic facial aging through time. Each sub-network only learns some specific features between two adjacent age groups.
        - This paper also introduces an age estimation loss to take into account the age distribution for an improved aging accuracy, and proposes to use the Pearson correlation coefficient as an evaluation metric measuring the aging smoothness for face aging methods. 
4. CycleGANs
    - Paper: https://arxiv.org/abs/1703.10593
    Video resources: 
    https://www.youtube.com/watch?v=-8hfnlxEPn4
    https://www.youtube.com/watch?v=NyAosnNQv_U
        - Learns mapping between input and output images using unpaired dataset
        - Cycle consistency: 
            - forward cycle-consistency loss x → G(x) → F(G(x)) ≈ x, and 
            - backward cycle-consistency loss: y → F(y) → G(F(y)) ≈ y
            - To summarize, our generator and discriminator will be able to generate some new images and be able to generate the old image back (forward). It will also be able to generate the old image from a novel image, and generate the novel image back (backward).
            - Loss function is a combination of the two losses in L1
        - We can perform style transfer using CycleGANs (i.e. simulating a rural environment with malnourished children, etc.)
    - Sample GitHub: https://github.com/HasnainRaz/Fast-AgingGAN
        - Face aging technology seems to work decently well, but the authors do not have examples of style transfer for simulating different environments.
