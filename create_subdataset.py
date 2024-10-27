import tarfile
import os
from PIL import Image

# Function to extract images from a tar.gz file
# Creates a subdataset for training, validation, and testing
# Saved in a folder named "extracted_images"
def extract_images(tar_path, output_dir, train_val_list_path, test_list_path, num_train=10, num_val=10, num_test=5):
    with open(train_val_list_path, 'r') as f:
        train_val_list = set(line.strip() for line in f)
    
    with open(test_list_path, 'r') as f:
        test_list = set(line.strip() for line in f)
    
    train_count, val_count, test_count = 0, 0, 0
    
    with tarfile.open(tar_path, 'r:gz') as tar:
        for member in tar.getmembers():
            if not member.name.lower().endswith(('.png', '.jpg', '.jpeg')):
                continue
            
            img_name = os.path.basename(member.name)
            
            if img_name in test_list and test_count < num_test:
                subset = 'test'
                subset_dir = os.path.join(output_dir, subset)
                img_path = os.path.join(subset_dir, img_name)
                
                if os.path.exists(img_path):
                    print(f"{img_name} already exists in {subset_dir}. Skipping.")
                    continue

                test_count += 1
            elif img_name in train_val_list:
                if train_count < num_train:
                    subset = 'train'
                elif val_count < num_val:
                    subset = 'val'
                else:
                    continue

                subset_dir = os.path.join(output_dir, subset)
                img_path = os.path.join(subset_dir, img_name)

                if os.path.exists(img_path):
                    print(f"{img_name} already exists in {subset_dir}. Skipping.")
                    continue

                if subset == 'train':
                    train_count += 1
                elif subset == 'val':
                    val_count += 1
            else:
                continue
            
            os.makedirs(subset_dir, exist_ok=True)
            
            img_file = tar.extractfile(member)
            if img_file:
                with Image.open(img_file) as img:
                    img.save(img_path)
            
            if train_count == num_train and val_count == num_val and test_count == num_test:
                break

# Extracting images from the tar.gz file
tar_path = 'images_004.tar.gz'
output_dir = 'extracted_images'
train_val_list_path = 'train_val-list.txt'
test_list_path = 'test_list.txt'
extract_images(tar_path, output_dir, train_val_list_path, test_list_path, num_train=10, num_val=10, num_test=5)
