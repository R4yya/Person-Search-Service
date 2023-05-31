import face_recognition
import numpy as np
from convert_image_to_bytes import get_project_path

# Аbsolute path of the project
project_path = get_project_path()

image_format = '.jpg'

# Load image
image_1 = face_recognition.load_image_file(
    f'{project_path}\\img\\test_me_1{image_format}')
image_2 = face_recognition.load_image_file(
    f'{project_path}\\img\\test_me_2{image_format}')

# Search for faces in images
face_locations_1 = face_recognition.face_locations(image_1)
face_locations_2 = face_recognition.face_locations(image_2)

# Get face encodings
face_encoding1 = np.array(
    face_recognition.face_encodings(image_1, face_locations_1))
face_encoding2 = np.array(
    face_recognition.face_encodings(image_2, face_locations_2))

# Compare face embeddings
# results = face_recognition.compare_faces(face_encoding1, face_encoding2)

# Calculate the distance between faces
face_distance = face_recognition.face_distance(
    [face_encoding1], face_encoding2)[0]

# Convert distance to similarity score
similarity_score = (1 - face_distance) * 100

# Print result
# if any(results):
#     print("The faces in the images converge")
# else:
#     print("The faces in the images do not converge")

# Print similarity score
print(f'Сходство {similarity_score:.2f}%')
