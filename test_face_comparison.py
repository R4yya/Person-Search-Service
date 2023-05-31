import face_recognition
import numpy as np
from convert_image_to_bytes import get_project_path

# Абсолютный путь проекта
project_path = get_project_path()

# Загрузка изображений из jpg
image1 = face_recognition.load_image_file(
    f'{project_path}\\img\\test_me_1.jpg')
image2 = face_recognition.load_image_file(
    f'{project_path}\\img\\test_me_2.jpg')

# Загрузка изображений из bin
# image1 = face_recognition.load_image_file(
#     f'{project_path}\\img_bytes\\test_durov_1.bin')
# image2 = face_recognition.load_image_file(
#     f'{project_path}\\img_bytes\\durov.bin')

# Поиск лиц на изображениях
face_locations1 = face_recognition.face_locations(image1)
face_locations2 = face_recognition.face_locations(image2)

# Получение признаков лиц
face_encoding1 = np.array(
    face_recognition.face_encodings(image1, face_locations1))
face_encoding2 = np.array(
    face_recognition.face_encodings(image2, face_locations2))

# Сравнение face embeddings
# results = face_recognition.compare_faces(face_encoding1, face_encoding2)

# Вычисление расстояния между лицами
face_distance = face_recognition.face_distance(
    [face_encoding1], face_encoding2)[0]

# Преобразование расстояния в процент уверенности
similarity_score = (1 - face_distance) * 100

# Вывод результата
# if any(results):
#     print("Лица на изображениях сходятся")
# else:
#     print("Лица на изображениях различаются")

# Вывод процента уверенности
print(f'Сходство {similarity_score:.2f}%')
