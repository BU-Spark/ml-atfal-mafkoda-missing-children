import argparse
import os
import sys
import glob
from deepface import DeepFace
import pandas as pd

class FaceRecognition:
    def __init__(self, metric='euclidean_l2', model='VGG-Face', missing_dir=None, unknown_dir=None, output_path=None):
        self.metric = metric
        self.model = model
        self.missing_dir = missing_dir
        self.unknown_dir = unknown_dir
        self.output_path = output_path
        self.metric_col = self.model + "_" + self.metric

        if self.output_path and os.path.exists(self.output_path):
            print('Output file already exists. choose another path') 
            print('press y to overwrite')
            choice = input()
            if choice.lower() != 'y':
                sys.exit('Recognition aborted')
    
    def run_on_directories(self):
        image_paths = glob.glob(os.path.join(self.missing_dir, "*"))
        results = []

        for path in image_paths:
            ext = os.path.splitext(path)[1].lower()
            if ext in [".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"]:
                dfs = DeepFace.find(
                    img_path=path,
                    db_path=self.unknown_dir, 
                    model_name=self.model,
                    distance_metric=self.metric
                )
                matched_filenames = ', '.join(dfs[0]['identity'].tolist())
                metric_values = ', '.join(map(str, dfs[0][self.metric_col].tolist()))

                results.append({
                    'missing_filename': path,
                    'unknowns_matched_filenames': matched_filenames,
                    self.metric_col: metric_values
                })

        # Convert results to a pandas DataFrame and save to CSV
        df = pd.DataFrame(results)
        df.to_csv(self.output_path, index=False)

def parse_args():
    parser = argparse.ArgumentParser(description='Face recognition')
    parser.add_argument('--model', required=False, type=str, default='VGG-Face', help='''
                        Model to use for Face Recognition 
                        Choices: [ VGG-Face , Facenet, Facenet512, OpenFace, DeepFace, DeepID, ArcFace, Dlib, SFace ]
                        ''')
    parser.add_argument('--metric', required=False, type=str, default='euclidean_l2', help='''
                        Metrics to use for Face Recognition
                        Choices: [ cosine, euclidean, euclidean_l2, euclidean_l1, euclidean_l2sq, manhattan, chebyshev, minkowski, mahalanobis, cosine_l2, cosine_l1, hamming ]
                        ''')
    parser.add_argument('--missing_dir', required=True, type=str, help='The directory containing images of missing persons')
    parser.add_argument('--unknown_dir', required=True, type=str, help='The directory containing images of unknown persons')
    parser.add_argument('--output_path', required=True, type=str, help='The path to the output CSV file')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    fr = FaceRecognition(
        metric=args.metric,
        model=args.model,
        missing_dir=args.missing_dir,
        unknown_dir=args.unknown_dir,
        output_path=args.output_path
    )
    fr.run_on_directories()