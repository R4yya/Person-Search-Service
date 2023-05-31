import face_recognition
import numpy as np
from convert_image_to_bytes import get_project_path

# Абсолютный путь проекта
project_path = get_project_path()

# Загрузка изображений из jpg
# image1 = face_recognition.load_image_file(f'{project_path}\\img\\gates.jpg')
# image2 = face_recognition.load_image_file(f'{project_path}\\img\\test_durov_1.jpg')

# Загрузка изображений из bin
image1 = face_recognition.load_image_file(
    f'{project_path}\\img_bytes\\test_durov_1.bin')
image2 = face_recognition.load_image_file(
    f'{project_path}\\img_bytes\\durov.bin')

# Поиск лиц на изображениях
face_locations1 = face_recognition.face_locations(image1)
face_locations2 = face_recognition.face_locations(image2)

# Получение face embeddings (признаки лиц)
face_embeddings1 = np.array(
    face_recognition.face_encodings(image1, face_locations1))
face_embeddings2 = np.array(
    face_recognition.face_encodings(image2, face_locations2))

# Сравнение face embeddings
results = face_recognition.compare_faces(face_embeddings1, face_embeddings2)

# Вывод результатов
if any(results):
    print("Лица на изображениях сходятся")
else:
    print("Лица на изображениях различаются")
