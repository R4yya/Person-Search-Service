from cv2 import imread, resize, cvtColor, \
    COLOR_BGR2GRAY, CascadeClassifier, rectangle, \
    imshow, waitKey, destroyAllWindows
from convert_image_to_bytes import get_project_path

# Аbsolute path of the project
project_path = get_project_path()

# Load image
image = imread(f'{project_path}\\img\\durov.jpg')

# Change image resolution
resized_image = resize(image, (640, 480))

# Convert an image to grayscale
gray_image = cvtColor(image, COLOR_BGR2GRAY)

# Search for faces in images
face_cascade = CascadeClassifier(
    f'{project_path}\\haar_cascades\\haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(
    gray_image, scaleFactor=1.1, minNeighbors=5)

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display an image with detected faces
imshow('Faces', image)
waitKey(0)
destroyAllWindows()
