from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QPixmap, QPainter, QPen
from PyQt6.QtWidgets import QMainWindow, QFileDialog
from PyQt6.QtCore import Qt, QStandardPaths


class AddRecordWindow(QMainWindow):
    def __init__(self,
                 session,
                 PersonsModel,
                 FaceDataModel,
                 PhotoHandler,
                 parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.retranslate_ui()
        self.session = session
        self.PersonsModel = PersonsModel
        self.FaceDataModel = FaceDataModel
        self.photo_handler = PhotoHandler
        self.selected_face_index = None

    def setup_ui(self):
        self.setObjectName('AddRecordWindow')
        self.setFixedSize(650, 450)

        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName('central_widget')
        self.setCentralWidget(self.central_widget)

        self.gridLayout = QtWidgets.QGridLayout(self.central_widget)
        self.gridLayout.setObjectName('gridLayout_edits')

        self.firstNameLabel = QtWidgets.QLabel(self.central_widget)
        self.firstNameLabel.setObjectName('firstNameLabel')
        self.gridLayout.addWidget(self.firstNameLabel, 0, 0, 1, 1)

        self.lastNameLabel = QtWidgets.QLabel(self.central_widget)
        self.lastNameLabel.setObjectName('lastNameLabel')
        self.gridLayout.addWidget(self.lastNameLabel, 1, 0, 1, 1)

        self.patronymicLabel = QtWidgets.QLabel(self.central_widget)
        self.patronymicLabel.setObjectName('patronymicLabel')
        self.gridLayout.addWidget(self.patronymicLabel, 2, 0, 1, 1)

        self.birthdateLabel = QtWidgets.QLabel(self.central_widget)
        self.birthdateLabel.setObjectName('birthdateLabel')
        self.gridLayout.addWidget(self.birthdateLabel, 3, 0, 1, 1)

        self.countryLabel = QtWidgets.QLabel(self.central_widget)
        self.countryLabel.setObjectName('countryLabel')
        self.gridLayout.addWidget(self.countryLabel, 4, 0, 1, 1)

        self.phoneNumberLabel = QtWidgets.QLabel(self.central_widget)
        self.phoneNumberLabel.setObjectName('phoneNumberLabel')
        self.gridLayout.addWidget(self.phoneNumberLabel, 5, 0, 1, 1)

        self.emailLabel = QtWidgets.QLabel(self.central_widget)
        self.emailLabel.setObjectName('emailLabel')
        self.gridLayout.addWidget(self.emailLabel, 6, 0, 1, 1)

        self.photoLabel = QtWidgets.QLabel(self.central_widget)
        self.photoLabel.setObjectName('photoLabel')
        self.gridLayout.addWidget(self.photoLabel, 0, 3, 7, 2)

        self.firstNameLineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.firstNameLineEdit.setObjectName('firstNameLineEdit')
        self.gridLayout.addWidget(self.firstNameLineEdit, 0, 1, 1, 1)

        self.lastNameLineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.lastNameLineEdit.setObjectName('lastNameLineEdit')
        self.gridLayout.addWidget(self.lastNameLineEdit, 1, 1, 1, 1)

        self.patronymicLineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.patronymicLineEdit.setObjectName('patronymicLineEdit')
        self.gridLayout.addWidget(self.patronymicLineEdit, 2, 1, 1, 1)

        self.birthdateDataEdit = QtWidgets.QDateEdit(self.central_widget)
        self.birthdateDataEdit.setObjectName('birthdateDataEdit')
        self.gridLayout.addWidget(self.birthdateDataEdit, 3, 1, 1, 1)

        self.countryLineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.countryLineEdit.setObjectName('countryLineEdit')
        self.gridLayout.addWidget(self.countryLineEdit, 4, 1, 1, 1)

        self.phoneNumberLineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.phoneNumberLineEdit.setObjectName('phoneNumberLineEdit')
        self.gridLayout.addWidget(self.phoneNumberLineEdit, 5, 1, 1, 1)

        self.emailLineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.emailLineEdit.setObjectName('emailLineEdit')
        self.gridLayout.addWidget(self.emailLineEdit, 6, 1, 1, 1)

        self.photoLineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.photoLineEdit.setObjectName('photoLineEdit')
        self.gridLayout.addWidget(self.photoLineEdit, 7, 3, 1, 1)

        self.facesComboBox = QtWidgets.QComboBox(self.central_widget)
        self.facesComboBox.setObjectName('facesComboBox')
        self.facesComboBox.currentIndexChanged.connect(self.combobox_activated)
        self.gridLayout.addWidget(self.facesComboBox, 8, 3, 1, 1)

        self.selectPhotoButton = QtWidgets.QPushButton(self.central_widget)
        self.selectPhotoButton.setObjectName('selectPhotoButton')
        self.selectPhotoButton.clicked.connect(self.select_image)
        self.gridLayout.addWidget(self.selectPhotoButton, 7, 4, 1, 1)

        self.addRecordButton = QtWidgets.QPushButton(self.central_widget)
        self.addRecordButton.setObjectName('addRecordButton')
        self.addRecordButton.clicked.connect(self.add_record)
        self.gridLayout.addWidget(self.addRecordButton, 8, 4, 1, 1)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate

        self.setWindowTitle(_translate('AddRecordWindow', 'Add record'))

        self.firstNameLabel.setText(_translate('AddRecordWindow', 'First name:'))
        self.lastNameLabel.setText(_translate('AddRecordWindow', 'Last name:'))
        self.patronymicLabel.setText(_translate('AddRecordWindow', 'Patronymic:'))
        self.birthdateLabel.setText(_translate('AddRecordWindow', 'Birthdate:'))
        self.countryLabel.setText(_translate('AddRecordWindow', 'Country:'))
        self.phoneNumberLabel.setText(_translate('AddRecordWindow', 'Phone number:'))
        self.emailLabel.setText(_translate('AddRecordWindow', 'E-mail:'))
        self.selectPhotoButton.setText(_translate('AddRecordWindow', 'Select photo'))
        self.addRecordButton.setText(_translate('AddRecordWindow', 'Add'))

    def select_image(self):
        file_dialog = QFileDialog()
        pictures_dir = QStandardPaths.writableLocation(
            QStandardPaths.StandardLocation.PicturesLocation)
        file_dialog.setDirectory(pictures_dir)

        image_path, _ = file_dialog.getOpenFileName(
            self, "Select Image", "", "Image Files (*.jpg *.png)")

        self.photoLineEdit.setText(image_path)

        self.pixmap = QPixmap(image_path)

        self.face_locations = self.get_all_faces()

        self.count_faces(self.face_locations)

        self.update_image_with_face()

    def update_image_with_face(self):
        image_path = self.get_image_path()
        pixmap = QPixmap(image_path)

        if self.selected_face_index is not None and self.selected_face_index >= 0:
            face_location = self.face_locations[self.selected_face_index]
            self.draw_rect(pixmap, face_location)

        self.photoLabel.setPixmap(pixmap)
        self.photoLabel.setScaledContents(True)
        self.resize(pixmap.width(), pixmap.height())

    def draw_rect(self, pixmap, face_location):
        painter = QPainter(pixmap)
        pen = QPen(Qt.GlobalColor.green)
        pen.setWidth(3)

        if face_location is not None:
            top, right, bottom, left = face_location

            painter.setPen(pen)
            painter.drawRect(left, top, right - left, bottom - top)
            painter.end()

    def combobox_activated(self, index):
        self.selected_face_index = index
        self.update_image_with_face()

    def get_image_path(self):
        return self.photoLineEdit.text()

    def get_image(self, image_path):
        image_path = self.get_image_path()

        return self.photo_handler.load_image(image_path)

    def get_all_faces(self):
        image_path = self.get_image_path()
        image = self.get_image(image_path)
        face_locations = self.photo_handler.get_face_locations(image)

        return face_locations

    def count_faces(self, new_face_locations):
        self.facesComboBox.clear()
        if len(new_face_locations) > 0:
            for i in range(len(new_face_locations)):
                self.facesComboBox.addItem(f'face_{i} {new_face_locations[i]}')
                self.selected_face_index = 0
            self.face_locations = new_face_locations
        else:
            self.selected_face_index = None
            self.face_locations = []

    def add_record(self):
        image = self.photo_handler.load_image(self.photoLineEdit.text())
        face_locations = self.photo_handler.get_face_locations(image)
        face_encodings = self.photo_handler.get_face_encodings(image, face_locations)

        if self.selected_face_index is not None and self.selected_face_index < len(face_locations):
            selected_face_location = face_locations[self.selected_face_index]
            selected_face_encoding = face_encodings[self.selected_face_index]

            person = self.PersonsModel(
                first_name=self.firstNameLineEdit.text(),
                last_name=self.lastNameLineEdit.text(),
                patronymic=self.patronymicLineEdit.text(),
                birthdate=self.birthdateDataEdit.date().toPyDate(),
                country=self.countryLineEdit.text(),
                phone_num=self.phoneNumberLineEdit.text(),
                email=self.emailLineEdit.text(),
                photo=self.photo_handler.get_image_bytes(self.photoLineEdit.text())
            )

            face_data = self.FaceDataModel(
                encoding=selected_face_encoding,
                location=list(selected_face_location),
                person=person
            )

            self.session.add(person)
            self.session.add(face_data)
            self.session.commit()

        self.hide()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    add_record_window = AddRecordWindow()
    add_record_window.show()

    sys.exit(app.exec())
