from PIL import Image
from convert_image_to_bytes import get_project_path

# Абсолютный путь проекта
project_path = get_project_path()

# Имя файла
file_name = input()

# Открываем изображения формата .png
image = Image.open(f'{get_project_path}\\img\\{file_name}.png')

# Сохранение изображение в формате .jpg
image.save(f'{get_project_path}\\img\\{file_name}.jpg')
