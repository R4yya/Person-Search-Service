import face_recognition
import numpy as np
from timeit import timeit
from convert_image_to_bytes import get_project_path


def load_images(image_format='.jpg'):
    # Аbsolute path of the project
    project_path = get_project_path()

    # Load image
    image_1 = face_recognition.load_image_file(
        f'{project_path}\\img\\durov{image_format}')
    image_2 = face_recognition.load_image_file(
        f'{project_path}\\img\\gates{image_format}')

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
        [face_encoding_1], face_encoding_2)

    return face_distances


def get_median(face_distances):
    # Calculate median of face_distances array
    median = np.median(face_distances)

    return median


def get_mean(face_distances):
    # Calculate arithmetic mean
    mean = np.mean(face_distances)

    return mean


def get_standard_deviation(face_distances):
    # Calculate standard deviation
    standard_deviation = np.std(face_distances)

    return standard_deviation


def get_face_recognition_accuracy(face_distance, face_match_threshold=0.6):
    if face_distance > face_match_threshold:
        match_threshold_range = (1.0 - face_match_threshold)
        linear_val = (1.0 - face_distance) / (match_threshold_range * 2.0)

        return linear_val
    else:
        match_threshold_range = face_match_threshold
        linear_val = 1.0 - (face_distance / (match_threshold_range * 2.0))

        return linear_val + ((1.0 - linear_val) * np.power((linear_val - 0.5) * 2, 0.2))


if __name__ == '__main__':
    # Load images get face encodings and distances
    image_1, image_2 = load_images()
    face_encoding_1, face_encoding_2 = get_face_encodings(image_1, image_2)
    face_distances = get_face_distances(face_encoding_1, face_encoding_2)

    # Print comparison result
    comparison_result = compare_faces(face_encoding_1, face_encoding_2)

    if any(comparison_result):
        print("The faces in the images converge\n")
    else:
        print("The faces in the images do not converge\n")

    # Print face distances
    print(f'{face_distances}\n')

    # Testing aggregation methods and their execution time
    # 1. Median
    similarity_score_median = get_median(face_distances)

    execution_time = timeit(lambda: get_median(face_distances), number=20)

    print('Median')
    print(f'Similarity is {similarity_score_median:.5f}')
    print(f'Execution time: {execution_time} seconds\n')

    # 2. Arithmetic mean
    similarity_score_mean = get_mean(face_distances)

    execution_time = timeit(lambda: get_mean(face_distances), number=20)

    print('Arithmetic mean')
    print(f'Similarity is {similarity_score_mean:.5f}')
    print(f'Execution time: {execution_time} seconds\n')

    # 3. Standard deviation
    similarity_score_sd = get_standard_deviation(face_distances)

    execution_time = timeit(
        lambda: get_standard_deviation(face_distances), number=20)

    print('Standard deviation')
    print(f'Similarity is {similarity_score_sd:.5f}')
    print(f'Execution time: {execution_time} seconds\n')

    # 4. face_recognition wikis solution
    # https://github.com/ageitgey/face_recognition/wiki/Calculating-Accuracy-as-a-Percentage
    # which is quite similar to face_recognition.compare_faces but returns
    # a sigle value
    similarity_score_fra = get_face_recognition_accuracy(get_median(face_distances))

    execution_time = timeit(
        lambda: get_face_recognition_accuracy(get_median(face_distances)), number=20)

    print('face_recognition wikis solution')
    print(f'Similarity is {similarity_score_fra}')
    print(f'Execution time: {execution_time} seconds')
