import face_recognition
import numpy as np
from convert_image_to_bytes import get_project_path
from timeit import timeit


def load_images(image_format='.jpg'):
    # Аbsolute path of the project
    project_path = get_project_path()

    # Load image
    image_1 = face_recognition.load_image_file(
        f'{project_path}\\img\\test_me_2{image_format}')
    image_2 = face_recognition.load_image_file(
        f'{project_path}\\img\\test_me_3{image_format}')

    return image_1, image_2


def get_face_encodings(image_1, image_2):
    # Search for faces in images
    face_locations_1 = face_recognition.face_locations(image_1)
    face_locations_2 = face_recognition.face_locations(image_2)

    # Get face encodings
    face_encoding_1 = np.array(
        face_recognition.face_encodings(image_1, face_locations_1))
    face_encoding_2 = np.array(
        face_recognition.face_encodings(image_2, face_locations_2))

    return face_encoding_1, face_encoding_2


def compare_faces(face_encoding_1, face_encoding_2):
    # Compare face embeddings
    comparison_result = face_recognition.compare_faces(
        face_encoding_1, face_encoding_2)

    return comparison_result


def get_face_distances(face_encoding_1, face_encoding_2):
    # Calculate the distance between faces
    face_distances = face_recognition.face_distance(
        [face_encoding_1], face_encoding_2)[0]

    return face_distances


def get_median(face_distances):
    # Calculate median of face_distances array
    median = np.median(face_distances)

    return (1 - median) * 100


def get_mean(face_distances):
    # Calculate arithmetic mean
    mean = np.mean(face_distances)

    return (1 - mean) * 100


def get_standard_deviation(face_distances):
    # Calculate standard deviation
    standard_deviation = np.std(face_distances)

    return (1 - standard_deviation) * 100


if __name__ == '__main__':
    # Load images get face encodings and distances
    image_1, image_2 = load_images()
    face_encoding_1, face_encoding_2 = get_face_encodings(image_1, image_2)
    face_distances = get_face_distances(face_encoding_1, face_encoding_2)

    # Print comparison result
    # comparison_result = compare_faces(face_encoding_1, face_encoding_2)
    # if any(comparison_result):
    #     print("The faces in the images converge")
    # else:
    #     print("The faces in the images do not converge")

    # Testing aggregation methods and their execution time
    # 1. Median
    similarity_score_median = get_median(face_distances)

    execution_time = timeit(lambda: get_median(face_distances), number=20)

    print('Median')
    print(f'Similarity is {similarity_score_median:.2f}%')
    print(f'Execution time: {execution_time} seconds\n')

    # 2. Arithmetic mean
    similarity_score_mean = get_mean(face_distances)

    execution_time = timeit(lambda: get_mean(face_distances), number=20)

    print('Arithmetic mean')
    print(f'Similarity is {similarity_score_mean:.2f}%')
    print(f'Execution time: {execution_time} seconds\n')

    # 3. Standard deviation
    similarity_score_sd = get_standard_deviation(face_distances)

    execution_time = timeit(
        lambda: get_standard_deviation(face_distances), number=20)

    print('Standard deviation')
    print(f'Similarity is {similarity_score_sd}%')
    print(f'Execution time: {execution_time} seconds')
