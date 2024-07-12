from PIL import Image
import os

def resize_images(folder_path, size=(640, 640)):
    # Ensure the folder path ends with a '/'
    if not folder_path.endswith('/'):
        folder_path += '/'
    
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    
    for file in files:
        # Check if the file is an image
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            img_path = os.path.join(folder_path, file)
            
            # Open the image
            with Image.open(img_path) as img:
                # Resize the image
                img_resized = img.resize(size, Image.LANCZOS)
                
                # Save the resized image back to the folder
                img_resized.save(img_path)
                print(f'Resized {file} and saved to {img_path}')

# Specify the folder containing the images
folder_path =r'/home/hbhcm/Downloads/new_data/dataset/dataset@1'

# Call the function to resize images
resize_images(folder_path)

