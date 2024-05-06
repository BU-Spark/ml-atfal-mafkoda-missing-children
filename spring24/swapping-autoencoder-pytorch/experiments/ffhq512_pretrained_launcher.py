from .tmux_launcher import Options, TmuxLauncher

class Launcher(TmuxLauncher):
    def options(self):
        opt = Options()
        opt.set(
            # I exported FFHQ dataset to 70,000 image files
            # and load them as images files.
            # Alternatively, the dataset can be prepared as
            # an LMDB dataset (like LSUN), and set dataset_mode = "lmdb".
            dataroot="/projectnb/sparkgrp/ml-atfal-mafkoda-grp/swapping-autoencoder-pytorch/datasets/ffhq/images1024x1024/",
            dataset_mode="imagefolder",
            checkpoints_dir="/projectnb/sparkgrp/ml-atfal-mafkoda-grp/swapping-autoencoder-pytorch/experiments/checkpoints/",
            num_gpus=1, 
            batch_size=16,
            preprocess="resize",
            load_size=512, crop_size=512,
        )

        return [
            opt.specify(
                name="ffhq512_pretrained",
            ),
        ]

    def train_options(self):
        common_options = self.options()
        return [opt.specify(
            continue_train=True,
            evaluation_metrics="swap_visualization",
            evaluation_freq=50000) for opt in common_options]
        
    def test_options(self, input_structure_image, input_texture_image):
        opt = self.options()[0]
        return [
            opt.tag("simple_swapping").specify(
                num_gpus=1,
                batch_size=1,
                dataroot=".",  # dataroot is ignored.
                result_dir="./results/",
                preprocess="scale_shortside",
                load_size=512,
                evaluation_metrics="simple_swapping",
                # Specify the two images here.
                input_structure_image=input_structure_image,
                input_texture_image=input_texture_image,
                # alpha == 1.0 corresponds to full swapping.
                # 0 < alpha < 1 means interpolation
                texture_mix_alpha=1.0,
            ),
            opt.tag("simple_interpolation").specify(
                num_gpus=1,
                batch_size=1,
                dataroot=".",  # dataroot is ignored.
                result_dir="./results/",
                preprocess="scale_shortside",
                load_size=512,
                evaluation_metrics="simple_swapping",
                # Specify the two images here.
                input_structure_image=input_structure_image,
                input_texture_image=input_texture_image,
                texture_mix_alpha='0.0 0.25 0.5 0.75 1.0',
            )
        ]
    
