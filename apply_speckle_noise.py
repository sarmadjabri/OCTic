import cv2
import numpy as np
import os
from skimage.util import random_noise

source_root = "images"
target_root = "speckle"

categories = ['CNV', 'DME', 'DRUSEN', 'NORMAL']

intensity_map = {
    'control': 0.0,
    '1': 0.1,
    '2': 0.2,
    '3': 0.3,
    '4': 0.4
}

os.makedirs(target_root, exist_ok=True)

if not os.path.exists(source_root):
    print(f"Error: Source root folder '{source_root}' does not exist.")
    exit()

for category in categories:
    cat_source_dir = os.path.join(source_root, category)
    
    if not os.path.exists(cat_source_dir):
        print(f"Skipping category '{category}': folder not found.")
        continue
        
    for subfolder, intensity in intensity_map.items():
        sub_source_dir = os.path.join(cat_source_dir, subfolder)
        sub_target_dir = os.path.join(target_root, category, subfolder)
        
        if not os.path.exists(sub_source_dir):
            print(f"Skipping subfolder '{category}/{subfolder}': folder not found.")
            continue
            
        os.makedirs(sub_target_dir, exist_ok=True)
        
        file_names = [f for f in os.listdir(sub_source_dir) if os.path.isfile(os.path.join(sub_source_dir, f))]
        print(f"Processing [{category} / {subfolder}] -> Variance: {intensity} ({len(file_names)} images)")
        
        for item in file_names:
            input_path = os.path.join(sub_source_dir, item)
            
            image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
            if image is None:
                continue
                
            image_float = image / 255.0
            
            if intensity == 0.0:
                processed_float = image_float
            else:
                processed_float = random_noise(image_float, mode='speckle', var=intensity)
                
            output_uint8 = np.clip(processed_float * 255, 0, 255).astype(np.uint8)
            output_path = os.path.join(sub_target_dir, item)
            cv2.imwrite(output_path, output_uint8)

print("\nBatch speckle noise generation completed successfully!")