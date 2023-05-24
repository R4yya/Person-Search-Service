from os import listdir
from os.path import dirname, splitext
from os.path import join as os_join
from cv2 import imread, imencode

# Абсолютный путь проекта
project_path = '\\'.join(dirname(__file__).split('\\')[:-1])

# Получение списка изображений в папке
images_list = listdir(f'{project_path}\\img')

# Обход каждого изображения
for image in images_list:
    # Полный путь к изображению
    image_path = os_join(f'{project_path}\\img', image)

    # Загрузка изображения с помощью OpenCV
    image_cv2 = imread(image_path)

    # Преобразование изображения в байтовый массив и вывод его в консоль
    image_bytes = (imencode('.jpg', image_cv2)[1].tobytes())

    # Имя выходного файла
    output_file = f'{splitext(image)[0]}.txt'

    # Полный путь к выходному файлу
    output_path = os_join(f'{project_path}\\img_bytes', output_file)

    # Запись байтов в файл
    with open(output_path, 'wb') as file:
        file.write(image_bytes)
