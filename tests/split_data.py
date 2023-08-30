import os
import shutil
import random

# source dir
original_data_dir = 'C:\\Users\\Isabelle\\Desktop\\HANDY\\data'

# train, val, test dirs
train_dir = os.path.join(original_data_dir, 'train')
validation_dir = os.path.join(original_data_dir, 'validation')
test_dir = os.path.join(original_data_dir, 'test')

# create the folders
os.makedirs(train_dir, exist_ok=True)
os.makedirs(validation_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# % of train/test/val
train_split = 0.6
validation_split = 0.25
test_split = 0.15

for category in ['offensive', 'notoffensive']:
    category_dir = os.path.join(original_data_dir, category)
    image_list = os.listdir(category_dir)
    random.shuffle(image_list)  # shuffle the images 

    num_images = len(image_list)

    num_train = int(train_split * num_images)
    num_validation = int(validation_split * num_images)

    train_images = image_list[:num_train]
    validation_images = image_list[num_train:num_train + num_validation]
    test_images = image_list[num_train + num_validation:]

    for image_name in train_images:
        src = os.path.join(category_dir, image_name)
        dst = os.path.join(train_dir, category, image_name)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy(src, dst)

    for image_name in validation_images:
        src = os.path.join(category_dir, image_name)
        dst = os.path.join(validation_dir, category, image_name)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy(src, dst)

    for image_name in test_images:
        src = os.path.join(category_dir, image_name)
        dst = os.path.join(test_dir, category, image_name)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy(src, dst)
