import argparse
import os
import sys
import glob
from deepface import DeepFace
import pandas as pd

class FaceRecognition:
    def __init__(self, args):
        self.args = args
        self.metric_col = self.args.model + "_" + self.args.metric
        if os.path.exists(self.args.output_path):
            print('Output file already exists. Choose another path.') 
            print('Press y to overwrite.')
            choice = input()
            if choice != 'y':
                sys.exit('Recognition aborted')

    def run_on_directories(self):
        image_paths = glob.glob(os.path.join(self.args.missing_dir, "*"))
        results = []

        for path in image_paths:
            ext = os.path.splitext(path)[1].lower()
            if ext in [".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"]:
                dfs = DeepFace.find(
                    img_path=path,
                    db_path=self.args.unknown_dir, 
                    model_name=self.args.model,
                    distance_metric=self.args.metric,
                )
                matched_filenames = ', '.join(dfs[0]['identity'].tolist())
                metric_values = ', '.join(map(str, dfs[0][self.metric_col].tolist()))

                results.append({
                    'missing_filename': path,
                    'unknowns_matched_filenames': matched_filenames,
                    self.metric_col: metric_values
                })

            df = pd.DataFrame(results)
            df.to_csv(self.args.output_path, index=False)

def parse_args():
    parser = argparse.ArgumentParser(description='Face recognition')
    parser.add_argument('--metric', required=False, type=str, default='euclidean_l2', help='The metric to use for face comparison choices: ')
    parser.add_argument('--model', required=False, type=str, default='VGG-Face', help='The model to use for face recognition')
    parser.add_argument('--missing_dir', required=True, type=str, help='The directory containing images of missing persons')
    parser.add_argument('--unknown_dir', required=True, type=str, help='The directory containing images of unknown persons')
    parser.add_argument('--output_path', required=True, type=str, help='The path to the output CSV file')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    fr = FaceRecognition(args)
    fr.run_on_directories()
