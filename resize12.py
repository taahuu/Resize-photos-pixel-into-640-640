import os
from PIL import Image

def resize_images(image_folder, output_folder=None, width=640, height=640):
  """Resizes all images in a folder to the specified dimensions.

  Args:
      image_folder (str): Path to the folder containing the images to resize.
      output_folder (str, optional): Path to the folder where resized images will be saved. Defaults to None, in which case they will be saved in the same folder as the originals.
      width (int, optional): Target width for resized images. Defaults to 640.
      height (int, optional): Target height for resized images. Defaults to 640.
  """

  # Create output folder if it doesn't exist
  if output_folder and not os.path.exists(output_folder):
    os.makedirs(output_folder)

  for filename in os.listdir(image_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):  # Check for common image formats
      image_path = os.path.join(image_folder, filename)
      try:
        img = Image.open(image_path)
        resized_img = img.resize((width, height), Image.LANCZOS)  # Use antialiasing for smoother resizing

        if output_folder:
          output_path = os.path.join(output_folder, filename)
        else:
          output_path = image_path  # Save in the same folder as the original

        resized_img.save(output_path, quality=95)  # Save with high quality (adjust as needed)
        print(f"Resized '{filename}' to {width}x{height}")
      except (IOError, OSError) as e:
        print(f"Error processing '{filename}': {e}")

# Example usage
image_folder = "/home/hbhcm/Downloads/new_data/dataset/dataset@1"  # Replace with your actual image folder path
resize_images(image_folder)  # Resizes images in the same folder (optional: specify output_folder)
