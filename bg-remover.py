import os
from PIL import Image
from rembg import remove

input_folder = 'input_images'  # The folder where the original images are stored
output_folder = 'output_images'  # The folder where you want to save the processed images

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate through every file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
        
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        # Open image and remove background
        with open(input_path, 'rb') as i:
            input_image = i.read()
            output_image = remove(input_image)
            
            # Save the processed image
            with open(output_path, 'wb') as o:
                o.write(output_image)

