from os import listdir
from os.path import dirname, splitext
from os.path import join as os_join
from cv2 import imread, imencode


def get_project_path():
    # Get absolute path of the project
    return '\\'.join(dirname(__file__).split('\\'))


def convert_image_to_bytes(image_path):
    # Load image with OpenCV
    image_cv2 = imread(image_path)

    # Convert an image to a byte array
    image_bytes = imencode('.jpg', image_cv2)[1].tobytes()

    return image_bytes


def write_bytes_to_file(output_path, image_bytes):
    # Write bytes to file
    with open(output_path, 'wb') as file:
        file.write(image_bytes)


def get_bytes_from_file(file_name):
    # Read bytes from file
    with open(os_join(f'{get_project_path()}\\img_bytes', file_name), 'rb') as file:
        return file.read()


if __name__ == '__main__':
    # Absolute path of the projec
    project_path = get_project_path()

    # Get list of images in folder
    images_list = listdir(f'{project_path}\\img')

    # Pass through each image
    for image in images_list:
        # Absolute path to image
        image_path = os_join(f'{project_path}\\img', image)

        # Convert an image to a byte array
        image_bytes = convert_image_to_bytes(image_path)

        # Name of output file
        output_file = f'{splitext(image)[0]}.bin'

        # Absolute path to output file
        output_path = os_join(f'{project_path}\\img_bytes', output_file)

        # Write bytes to file
        write_bytes_to_file(output_path, image_bytes)
