from PIL import Image
from convert_image_to_bytes import get_project_path


def convert_image(file_name):
    # Аbsolute path of the project
    project_path = get_project_path()

    # Open image in .png format
    image = Image.open(f'{project_path}\\img\\{file_name}.png')

    # Save image in .jpg format
    image.save(f'{project_path}\\img\\{file_name}.jpg')
