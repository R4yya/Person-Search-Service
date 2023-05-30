from cv2 import imread, resize, cvtColor, \
    COLOR_BGR2GRAY, CascadeClassifier, rectangle, \
    imshow, waitKey, destroyAllWindows
from convert_image_to_bytes import get_project_path

# Абсолютный путь проекта
project_path = get_project_path()

# Загрузка изображения
image = imread(f'{project_path}\\img\\durov.jpg')

# Изменение размера изображения
resized_image = resize(image, (640, 480))

# Преобразование изображения в оттенки серого
gray_image = cvtColor(image, COLOR_BGR2GRAY)

# Обнаружение лиц на изображении
face_cascade = CascadeClassifier(
    f'{project_path}\\haar_cascades\\haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(
    gray_image, scaleFactor=1.1, minNeighbors=5)

# Отрисовка прямоугольников вокруг обнаруженных лиц
for (x, y, w, h) in faces:
    rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Отображение изображения с обнаруженными лицами
imshow('Faces', image)
waitKey(0)
destroyAllWindows()
