import os
import requests
import json
from PIL import Image, ImageDraw
import argparse
import csv


class DataDownloader:
    def __init__(self, json_path=None, base_folder=None):
        self.json_path = json_path
        self.base_folder = base_folder
        if not self.json_path or not self.base_folder:
            self.parse_args()

    def parse_args(self):
        parser = argparse.ArgumentParser(description='Process images based on provided JSON data.')
        parser.add_argument('-j', '--json', required=True, help='Path to the JSON data file.')
        parser.add_argument('-o', '--output', required=True, help='Directory where the images and missing data will be saved.')
        args = parser.parse_args()
        self.json_path = args.json
        self.base_folder = args.output

    def download_image(self, url, path):
        response = requests.get(url, stream=True)
        with open(path, 'wb') as out_file:
            out_file.write(response.content)

    def check_missing_keys(self, dictionary, required_keys):
        missing_keys = []
        for key in required_keys:
            if key not in dictionary or dictionary[key] is None:
                missing_keys.append(key)
        return missing_keys

    def run(self):
        if os.path.exists(self.base_folder):
            overwrite = input("Output directory already exists. Press 'y' to overwrite: ")
            if overwrite.lower() != 'y':
                print("Operation aborted by the user.")
                return

        if not os.path.exists(self.base_folder):
            os.mkdir(self.base_folder)

        with open(self.json_path, "r") as file:
            data = json.load(file)

        required_case_keys = ["case_status", "id", "posts"]
        required_post_keys = ["photos"]
        required_photo_keys = ["preview_url", "face_boxes", "enhanced_faces"]

        csv_path = os.path.join(self.base_folder, 'missing_data.csv')

        with open(csv_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Type', 'Case ID', 'Post Index', 'Photo Index', 'Missing Keys'])

            for case in data:
                missing_case_keys = self.check_missing_keys(case, required_case_keys)
                if missing_case_keys:
                    csv_writer.writerow(['Case', case.get('id', 'Unknown'), '', '', ', '.join(missing_case_keys)])
                    continue

                case_status_folder = os.path.join(self.base_folder, case["case_status"])
                case_id_folder = os.path.join(case_status_folder, case["id"])
                os.makedirs(case_id_folder, exist_ok=True)

                for index, post in enumerate(case["posts"]):
                    missing_post_keys = self.check_missing_keys(post, required_post_keys)
                    if missing_post_keys:
                        csv_writer.writerow(['Post', case['id'], index, '', ', '.join(missing_post_keys)])
                        continue

                    photos_folder = os.path.join(case_id_folder, "photos")
                    enhanced_folder = os.path.join(case_id_folder, "enhanced")
                    photos_boxed_folder = os.path.join(case_id_folder, "photos_boxed")
                    enhanced_boxed_folder = os.path.join(case_id_folder, "enhanced_boxed")

                    os.makedirs(photos_folder, exist_ok=True)
                    os.makedirs(enhanced_folder, exist_ok=True)
                    os.makedirs(photos_boxed_folder, exist_ok=True)
                    os.makedirs(enhanced_boxed_folder, exist_ok=True)

                    for photo_index, photo in enumerate(post["photos"]):
                        missing_photo_keys = self.check_missing_keys(photo, required_photo_keys)
                        if missing_photo_keys:
                            csv_writer.writerow(['Photo', case['id'], index, photo_index, ', '.join(missing_photo_keys)])
                            continue

                        photo_path = os.path.join(photos_folder, f"{case['id']}_photos_{photo_index}.jpg")
                        self.download_image(photo["preview_url"], photo_path)

                        for enhanced_index, enhanced in enumerate(photo["enhanced_faces"]):
                            enhanced_path = os.path.join(enhanced_folder, f"{case['id']}_enhanced_{enhanced_index}.png")
                            self.download_image(enhanced["signed_url"], enhanced_path)

                        img = Image.open(photo_path)
                        draw = ImageDraw.Draw(img)
                        for face_box in eval(photo["face_boxes"]):
                            draw.rectangle([face_box["x1"], face_box["y1"], face_box["x2"], face_box["y2"]], outline="red")
                        img.save(os.path.join(photos_boxed_folder, f"{case['id']}_photos_boxed_{photo_index}.jpg"))

                        for enhanced_index, enhanced in enumerate(photo["enhanced_faces"]):
                            img = Image.open(os.path.join(enhanced_folder, f"{case['id']}_enhanced_{enhanced_index}.png"))
                            draw = ImageDraw.Draw(img)
                            face_box = eval(enhanced["original_face_box"])
                            draw.rectangle([face_box["x1"], face_box["y1"], face_box["x2"], face_box["y2"]], outline="red")
                            img.save(os.path.join(enhanced_boxed_folder, f"{case['id']}_enhanced_boxed_{enhanced_index}.png"))

        print("Completed!")


if __name__ == "__main__":
    downloader = DataDownloader()
    downloader.run()
