from PIL import Image
from convert_image_to_bytes import get_project_path

# Аbsolute path of the project
project_path = get_project_path()

# File name
file_name = input()

# Open image in .png format
image = Image.open(f'{get_project_path}\\img\\{file_name}.png')

# Save image in .jpg format
image.save(f'{get_project_path}\\img\\{file_name}.jpg')
