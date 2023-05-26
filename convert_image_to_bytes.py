from os import listdir
from os.path import dirname, splitext
from os.path import join as os_join
from cv2 import imread, imencode


def get_project_path():
    # Абсолютный путь проекта
    return '\\'.join(dirname(__file__).split('\\'))


def convert_image_to_bytes(image_path):
    # Загрузка изображения с помощью OpenCV
    image_cv2 = imread(image_path)

    # Преобразование изображения в байтовый массив
    image_bytes = imencode('.jpg', image_cv2)[1].tobytes()

    return image_bytes


def write_bytes_to_file(output_path, image_bytes):
    # Запись байтов в файл
    with open(output_path, 'wb') as file:
        file.write(image_bytes)


def get_bytes_from_file(file_name):
    with open(os_join(f'{get_project_path()}\\img_bytes', file_name), 'rb') as file:
        return file.read()


# Получение списка изображений в папке
images_list = listdir(f'{get_project_path()}\\img')

# Обход каждого изображения
for image in images_list:
    # Полный путь к изображению
    image_path = os_join(f'{get_project_path()}\\img', image)

    # Преобразование изображения в байтовый массив
    image_bytes = convert_image_to_bytes(image_path)

    # Имя выходного файла
    output_file = f'{splitext(image)[0]}.bin'

    # Полный путь к выходному файлу
    output_path = os_join(f'{get_project_path()}\\img_bytes', output_file)

    # Запись байтов в файл
    write_bytes_to_file(output_path, image_bytes)