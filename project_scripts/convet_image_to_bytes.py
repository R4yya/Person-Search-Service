from activate_venv import activate_myvenv
import cv2

# Активация виртуального окружения
activate_myvenv()

# Загрузка изображения с помощью OpenCV
image = cv2.imread('img/durov.jpg')

# Преобразование изображения в байтовый массив и вывод его в консоль
print(cv2.imencode('.jpg', image)[1].tobytes())
