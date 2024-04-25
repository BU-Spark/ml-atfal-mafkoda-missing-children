**Research**

1. PFA-GAN: Progressive Face Aging With Generative Adversarial Network
    - Key Takeaways:
        - By utilizing a GAN with multiple subnetworks, the PFA-GAN ages adjacent age groups to accurately age images using the philosophy that aging effects are different from different age groups
        - This method also improves aging quality, accuracy and identity preservation
        - Traditional methods use the target age group as a conditional input, while this method proposes a novel age encoding scheme that adds binary gates to control the aging flow
    - Github: [https://github.com/Hzzone/PFA-GAN]

2. FA-GAN: Face Augmentation GAN for Deformation-Invariant Face Recognition [https://ieeexplore.ieee.org/abstract/document/9330536]
    - Key Takeaways: 
        - FA-GAN with two branches: One has a geometric preserving model that learns geometry information to preserve spatial and semantic relations. The other branch has a Face Disentanglement Module and for deforming some of the faces.
        - This method has been proven effective in unconstrained environments.

3. FaceID-GAN: Learning a Symmetry Three-Player GAN for Identity-Preserving Face Synthesis: [https://openaccess.thecvf.com/content_cvpr_2018/html/Shen_FaceID-GAN_Learning_a_CVPR_2018_paper.html]
    - Key Takeaways:
        - Identity preserving GANs can be created by adding a third player, which competes with the generator by distinguishing identities of real and synthesized faces. Rather than making identity classifier a additional discriminator, FaceID-Gan formulated by satisfying information symmetry, meaning the real and synthesized images are projected into the same feature space (which allows for easier training).
        - Compared to other existing methods, which extend GAN by using an additional classifier and predicts their identity labels, FaceID-GAN turn two-player GAN to GAN with three players. Other methods treat C as spectator which doesn’t compete with G. C competes with G and cooperates with D.
        - Issue with previous method is that it does create the same identity but as long as C can distinguish who it is compared to other N subjects, it doesn’t get better. By making C directly compete with G, it forces G to produce as close to the person as possible.
        - Main purpose of this paper is that it can create faces of arbitrary viewpoints and expressions.
    - Github: Official github not released (Someone tried recreating this [https://github.com/shoutOutYangJie/FaceID-GAN])

4. GAN-Based Facial Attribute Manipulation: [https://ieeexplore.ieee.org/abstract/document/10194986]
    - Key Takeaways:
        - Study of existing GAN-based FAM studies (Facial Attribute Manipulation).
        - GANs are the best ways to perform FAM and outperforms deep networks (which look worse) and older methods (which have complicated algorithm pipelines).
        - Provides many datasets and different type of evaluation metrics used for FAM.
        - Provides introduction on two-domain, multi-domain model, types of constraints, and the types of methodologies used for GAN-based FAMs
        - Provides plenty of GANs specifically made for FAM

5. BeautyGAN: Instance-level Facial Makeup Transfer with Deep Generative Adversarial Network: https://dl.acm.org/doi/abs/10.1145/3240508.3240618
    - Key Takeaways:
        - Just like our issue, this study deals with no paired data, deals with transferring non-global styles (i.e. paintings) that can consist of several local styles. Extracting and transferring such local information is addressed here
        - This is done with a global domain-level loss and local instance-level loss in dual input/output GAN. Domain-level focuses on usual discriminators that distinguish real from generated images. Instance-level calculates a pixel-level histogram loss on separate local facial regions. This is done with perceptual loss and cycle consistency loss to preserve identity
        - This means both the no makeup image and makeup image are both inserted and generates its corresponding makeup and no makeup version. 
        - When coming to Instance-level makeup transfer, it uses three attributes as the three important components and has to do with color. This means the model uses a face parsing model that separates the lip, eyes, and face. The loss is calculated by comparing colors as they determine color-changing as the main component of makeup.
    - Github: [https://github.com/jonhyuk0922/01.BeautyGAN]

6. L2M-GAN: Learning to Manipulate Latent Space Semantics for Facial Attribute Editing: [https://openaccess.thecvf.com/content/CVPR2021/html/Yang_L2M-GAN_Learning_To_Manipulate_Latent_Space_Semantics_for_Facial_Attribute_CVPR_2021_paper.html]
    - Key Takeaways:
        - Proposing latent space factorization model for editing both local and global features
        - New style transformer of two modules: a decomposer for disentangling the source style code into two orthogonal parts (attribute relevant and attribute irrelevant), a domain transformer for transforming the attribute-relevant code from its original domain to target
        - L2M-GAN explicitly factorizes the latent space vector of a GAN into attribute-relevant and -irrelevant codes.
    - Github: [https://github.com/rucmlcv/L2M-GAN]

7. A Style-Based Generator Architecture for Generative Adversarial Networks: https://arxiv.org/pdf/1812.04948v3.pdf
    - Key Takeaways:
        - Proposes a GAN that better disentangles the latent factors of variation
        - Automatically learned, unsupervised separation of high-level features
        - New generator starts from a learned constant input and adjusts the “style” of the image at each convolution layer
        - Omits input layer and starts from a learned constant
        - Incorporates mixing regularization to decor relate neighboring styles
    - Github: [https://github.com/NVlabs/stylegan]

8. P2-GAN: Efficient Style Transfer Using Single Style Image: [https://arxiv.org/pdf/2001.07466.pdf]
    - Key Takeaways:
        - A novel Patch Permutation GAN (P2-GAN) network that can efficiently learn the stroke style from a single style image is proposed.
        - Path permutation used to generate multiple samples from a given style image.
        - Discriminator simultaneously processes the patch-wise images.
    - Github: [https://github.com/i-evi/p2gan]
