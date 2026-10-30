import os
import shutil
import random


SOURCE_FOLDER = "Path\to\folder"
X = 0 #<- number of files (has to be divisible by 5)


FOLDER_NAMES = ["control", "1", "2", "3", "4"]
NUM_FOLDERS = len(FOLDER_NAMES)


def split_images():

    if X % NUM_FOLDERS != 0:
        print(
            f"Error: X ({X}) is not evenly divisible by {NUM_FOLDERS}. "
            f"Each folder needs an equal number of images."
        )
        return

    images_per_folder = int(X/5)
    valid_extensions = (".jpg", ".jpeg", ".JPG", ".JPEG")
    all_files = [
        f
        for f in os.listdir(SOURCE_FOLDER)
        if f.endswith(valid_extensions)
        and os.path.isfile(os.path.join(SOURCE_FOLDER, f))
    ]


    if len(all_files) < X:
        print(
            f"Error: You requested X={X} images, but only found {len(all_files)} JPEGs in the folder."
        )
        return


    random.shuffle(all_files)


    selected_images = all_files[:X]


    for folder in FOLDER_NAMES:
        target_path = os.path.join(SOURCE_FOLDER, folder)
        os.makedirs(target_path, exist_ok=True)


    for i, file_name in enumerate(selected_images):

        folder_index = i // images_per_folder
        target_folder = FOLDER_NAMES[folder_index]


        src_path = os.path.join(SOURCE_FOLDER, file_name)
        dst_path = os.path.join(SOURCE_FOLDER, target_folder, file_name)


        shutil.move(src_path, dst_path)

    print(
        f"Successfully split {X} images evenly into 'control', '1', '2', '3', and '4'."
    )
    print(f"Each folder received {images_per_folder} images.")


if __name__ == "__main__":
    split_images()
