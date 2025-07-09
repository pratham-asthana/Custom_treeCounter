import os
import shutil
import random

images_dir = "images"
labels_dir = "labels"

output_base = "dataset"
split_ratio = 0.8  


for split in ["train", "val"]:
    os.makedirs(os.path.join(output_base, "images", split), exist_ok=True)
    os.makedirs(os.path.join(output_base, "labels", split), exist_ok=True)


image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]
random.shuffle(image_files)

split_index = int(len(image_files) * split_ratio)
train_images = image_files[:split_index]
val_images = image_files[split_index:]

def move_files(file_list, split):
    for file_name in file_list:
        image_path = os.path.join(images_dir, file_name)
        label_path = os.path.join(labels_dir, os.path.splitext(file_name)[0] + ".txt")

        shutil.copy(image_path, os.path.join(output_base, "images", split, file_name))

        if os.path.exists(label_path):
            shutil.copy(label_path, os.path.join(output_base, "labels", split, os.path.basename(label_path)))


move_files(train_images, "train")
move_files(val_images, "val")
print(f"Dataset split completed. {len(train_images)} train and {len(val_images)} val images.")
