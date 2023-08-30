import os

# train/val/dir directories
train_dir = 'C:\\Users\\Isabelle\\Desktop\\HANDY\\data\\train'
validation_dir = 'C:\\Users\\Isabelle\\Desktop\\HANDY\\data\\validation'
test_dir = 'C:\\Users\\Isabelle\\Desktop\\HANDY\\data\\test'

# counting images for each dir
def count_images_in_directory(directory):
    class_counts = {}  # Dicionário para armazenar contagem de cada classe
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            class_path = os.path.join(root, dir)
            num_images = len(os.listdir(class_path))
            class_counts[dir] = num_images
    return class_counts

# implementation
train_class_counts = count_images_in_directory(train_dir)
validation_class_counts = count_images_in_directory(validation_dir)
test_class_counts = count_images_in_directory(test_dir)


print("Training images per class:")
for class_name, count in train_class_counts.items():
    print(f"{class_name}: {count} images")

print("\nValidation images per class:")
for class_name, count in validation_class_counts.items():
    print(f"{class_name}: {count} images")

print("\nTest images per class:")
for class_name, count in test_class_counts.items():
    print(f"{class_name}: {count} images")
