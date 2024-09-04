import os
import glob
import shutil
import random

# Define the paths
input_dir = 'labelme'
output_dir = 'dataset'
train_dir = os.path.join(output_dir, 'train')
val_dir = os.path.join(output_dir, 'val')
test_dir = os.path.join(output_dir, 'test')

# Create the output directories
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Get all the image files and corresponding label files
image_files = glob.glob(os.path.join(input_dir, '*.jpg'))
label_files = [f.replace('.jpg', '.json') for f in image_files]

# Combine image and label files into pairs
file_pairs = list(zip(image_files, label_files))

# Shuffle the file pairs
random.shuffle(file_pairs)

# Calculate the split indices
total_files = len(file_pairs)
train_split = int(0.6 * total_files)
val_split = int(0.2 * total_files)

# Split the file pairs into train, val, and test sets
train_files = file_pairs[:train_split]
val_files = file_pairs[train_split:train_split + val_split]
test_files = file_pairs[train_split + val_split:]

# Function to copy files to the target directory
def copy_files(file_pairs, target_dir):
    for img_file, label_file in file_pairs:
        shutil.copy(img_file, target_dir)
        shutil.copy(label_file, target_dir)

# Copy the files to the respective directories
copy_files(train_files, train_dir)
copy_files(val_files, val_dir)
copy_files(test_files, test_dir)

print("Dataset split completed.")