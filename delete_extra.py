import os

# Folder path containing both images and txt files
folder_path = r"D:\cvat\y_c_morning_frames"


# Get all the files in the folder
files = os.listdir(folder_path)

# Separate image and text files based on their extensions
image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
txt_files = [f for f in files if f.lower().endswith('.txt')]

# Create a set of filenames without extensions for comparison
txt_names = set(os.path.splitext(f)[0] for f in txt_files)

# Loop through image files and delete the ones without matching txt files
for image in image_files:
    image_name = os.path.splitext(image)[0]
    if image_name not in txt_names:
        image_path = os.path.join(folder_path, image)
        print(f"Deleting {image_path}")
        os.remove(image_path)  # Delete the image file
