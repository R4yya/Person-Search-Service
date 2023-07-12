import face_recognition
import numpy as np
from convert_image_to_bytes import get_project_path


def load_images(img_1, img_2, image_format='.jpg'):
    # Аbsolute path of the project
    project_path = get_project_path()

    # Load image
    image_1 = face_recognition.load_image_file(
        f'{project_path}\\img\\{img_1}{image_format}')
    image_2 = face_recognition.load_image_file(
        f'{project_path}\\img\\{img_2}{image_format}')

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


# def get_median(face_distances):
#     # Calculate median of face_distances array
#     median = np.median(face_distances)

#     return median


# def get_mean(face_distances):
#     # Calculate arithmetic mean
#     mean = np.mean(face_distances)

#     return mean


# def get_standard_deviation(face_distances):
#     # Calculate standard deviation
#     standard_deviation = np.std(face_distances)

#     return standard_deviation


# def get_face_recognition_accuracy(face_distances, face_match_threshold=0.6):
#     # face_recognition wikis modified solution
#     # https://github.com/ageitgey/face_recognition/wiki/Calculating-Accuracy-as-a-Percentage
#     # which is quite similar to face_recognition.compare_faces but returns a sigle value
#     confidences = []
#     for distance in np.nditer(face_distances):
#         if distance > face_match_threshold:
#             match_threshold_range = (1.0 - face_match_threshold)
#             linear_val = (1.0 - distance) / (match_threshold_range * 2.0)
#             confidence = linear_val

#             return linear_val
#         else:
#             match_threshold_range = face_match_threshold
#             linear_val = 1.0 - (distance / (match_threshold_range * 2.0))
#             confidence = linear_val + \
#                 ((1.0 - linear_val) * ((linear_val - 0.5) * 2) ** 0.2)
#         confidences.append(confidence)
#     return np.array(confidences)


# def match_percentage(face_distances):
#     face_match_percentage = (1 - face_distances[0]) * 100
#     for i, face_distances in enumerate(face_distances):
#         print(
#             f'The test image has a distance of {face_distances} from known image #{i}')

#         print(f'- comparing with a tolerance of 0.6? {face_distances < 0.6}')

#         print(np.round(face_match_percentage, 4))  # upto 4 decimal places


# def calculate_similarity_percentage_1(face_distances, face_match_threshold=0.6):
#     similarity = 1 - (face_distances - face_match_threshold) / \
#         (1 - face_match_threshold)
#     similarity = np.clip(similarity, 0, 1)  # limit in range [0, 1]
#     similarity_percentage = np.mean(similarity * 100)

#     return similarity_percentage


# def calculate_similarity_percentage_2(face_distances, threshold=0.6):
#     normalized_distances = [(d - min(face_distances)) /
#                             (max(face_distances) - min(face_distances)) for d in face_distances]
#     similarity_count = sum(1 for d in normalized_distances if d < threshold)
#     similarity_percentage = (similarity_count / len(face_distances)) * 100

#     return similarity_percentage


# def calculate_similarity_percentage_3(face_distances):
#     return np.mean(np.exp(-10 * face_distances))


# def calculate_similarity_percentage_4(face_distances):
#     return 1 / (1 + face_distances)


if __name__ == '__main__':
    # Load images get face encodings and distances
    image_1, image_2 = load_images('test_me_1', 'test_durov_3')
    face_encoding_1, face_encoding_2 = get_face_encodings(image_1, image_2)
    face_distances = get_face_distances(face_encoding_1, face_encoding_2)

    # Print comparison result
    comparison_result = compare_faces(face_encoding_1, face_encoding_2)

    if any(comparison_result):
        print(f'The faces in the images converge\n')
    else:
        print(f'The faces in the images do not converge\n')

    # Print face distances
    print(f'{face_distances}\n')
