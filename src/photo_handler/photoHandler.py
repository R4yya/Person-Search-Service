from PIL import Image
from io import BytesIO
import face_recognition as fr
import numpy as np


class PhotoHandler(object):
    def __init__(self):
        pass

    def get_image_bytes(self, path):
        image = Image.open(path)

        bytes_stream = BytesIO()

        image.save(bytes_stream, format='JPEG')

        byte_array = bytes_stream.getvalue()

        return byte_array

    def load_image(self, path):
        image = fr.load_image_file(path)

        return image

    def get_face_locations(self, image):
        face_locations = fr.face_locations(image)

        return face_locations

    def get_face_encodings(self, image, face_locations):
        face_encodings = fr.face_encodings(image, face_locations)
        face_encodings = [encoding.tolist() for encoding in face_encodings]

        return face_encodings

    def get_face_distances(self, face_encoding_1, face_encoding_2):
        face_distances = fr.face_distance([face_encoding_1], face_encoding_2)

        return face_distances

    def compare_faces(self, face_encoding_1, face_encoding_2):
        comparison_result = fr.compare_faces(face_encoding_1, face_encoding_2)

        return comparison_result

    def search_faces(self, path, all_face_data):
        target_image = self.load_image(path)
        target_locations = self.get_face_locations(target_image)
        target_encoding = self.get_face_encodings(target_image, target_locations)[0]

        face_encodings = [face_data.encoding for face_data in all_face_data]
        face_identifiers = [face_data.person_id for face_data in all_face_data]

        similarities = fr.compare_faces(np.array(face_encodings),
                                        np.array(target_encoding))

        similar_face_identifiers = [face_identifiers[i] for i, is_similar in enumerate(similarities) if is_similar]

        return similar_face_identifiers
