from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QFileDialog
from PyQt6.QtCore import Qt, QStandardPaths


class FindPersonWindow(QMainWindow):
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

    def setup_ui(self):
        self.setObjectName('FindPersonWindow')
        self.setFixedSize(250, 400)

        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName('central_widget')
        self.setCentralWidget(self.central_widget)

        self.gridLayout = QtWidgets.QGridLayout(self.central_widget)
        self.gridLayout.setObjectName('gridLayout_edits')

        self.firstNameLabel = QtWidgets.QLabel(self.central_widget)
        self.firstNameLabel.setObjectName('firstNameLabel')
        self.gridLayout.addWidget(self.firstNameLabel, 2, 0, 1, 1)

        self.lastNameLabel = QtWidgets.QLabel(self.central_widget)
        self.lastNameLabel.setObjectName('lastNameLabel')
        self.gridLayout.addWidget(self.lastNameLabel, 3, 0, 1, 1)

        self.patronymicLabel = QtWidgets.QLabel(self.central_widget)
        self.patronymicLabel.setObjectName('patronymicLabel')
        self.gridLayout.addWidget(self.patronymicLabel, 4, 0, 1, 1)

        self.birthdateLabel = QtWidgets.QLabel(self.central_widget)
        self.birthdateLabel.setObjectName('birthdateLabel')
        self.gridLayout.addWidget(self.birthdateLabel, 5, 0, 1, 1)

        self.countryLabel = QtWidgets.QLabel(self.central_widget)
        self.countryLabel.setObjectName('countryLabel')
        self.gridLayout.addWidget(self.countryLabel, 6, 0, 1, 1)

        self.phoneNumberLabel = QtWidgets.QLabel(self.central_widget)
        self.phoneNumberLabel.setObjectName('phoneNumberLabel')
        self.gridLayout.addWidget(self.phoneNumberLabel, 7, 0, 1, 1)

        self.emailLabel = QtWidgets.QLabel(self.central_widget)
        self.emailLabel.setObjectName('emailLabel')
        self.gridLayout.addWidget(self.emailLabel, 8, 0, 1, 1)

        self.firstNameLineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.firstNameLineEdit.setObjectName('firstNameLineEdit')
        self.gridLayout.addWidget(self.firstNameLineEdit, 2, 1, 1, 1)

        self.lastNameLineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.lastNameLineEdit.setObjectName('lastNameLineEdit')
        self.gridLayout.addWidget(self.lastNameLineEdit, 3, 1, 1, 1)

        self.patronymicLineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.patronymicLineEdit.setObjectName('patronymicLineEdit')
        self.gridLayout.addWidget(self.patronymicLineEdit, 4, 1, 1, 1)

        self.birthdateDataEdit = QtWidgets.QDateEdit(self.central_widget)
        self.birthdateDataEdit.setObjectName('birthdateDataEdit')
        self.gridLayout.addWidget(self.birthdateDataEdit, 5, 1, 1, 1)

        self.countryLineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.countryLineEdit.setObjectName('countryLineEdit')
        self.gridLayout.addWidget(self.countryLineEdit, 6, 1, 1, 1)

        self.phoneNumberLineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.phoneNumberLineEdit.setObjectName('phoneNumberLineEdit')
        self.gridLayout.addWidget(self.phoneNumberLineEdit, 7, 1, 1, 1)

        self.emailLineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.emailLineEdit.setObjectName('emailLineEdit')
        self.gridLayout.addWidget(self.emailLineEdit, 8, 1, 1, 1)

        self.photoLineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.photoLineEdit.setObjectName('photoLineEdit')
        self.gridLayout.addWidget(self.photoLineEdit, 0, 0, 1, 1)

        self.selectPhotoButton = QtWidgets.QPushButton(self.central_widget)
        self.selectPhotoButton.setObjectName('selectPhotoButton')
        self.selectPhotoButton.clicked.connect(self.select_image)
        self.gridLayout.addWidget(self.selectPhotoButton, 0, 1, 1, 1)

        self.findPhotoButton = QtWidgets.QPushButton(self.central_widget)
        self.findPhotoButton.setObjectName('findPhotoButton')
        self.findPhotoButton.clicked.connect(self.display_search_results)
        self.gridLayout.addWidget(self.findPhotoButton, 1, 1, 1, 1)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate

        self.setWindowTitle(_translate('FindPersonWindow', 'Find person'))
        self.selectPhotoButton.setText(_translate('FindPersonWindow', 'Select'))
        self.findPhotoButton.setText(_translate('FindPersonWindow', 'Find'))
        self.firstNameLabel.setText(_translate('FindPersonWindow', 'First name:'))
        self.lastNameLabel.setText(_translate('FindPersonWindow', 'Last name:'))
        self.patronymicLabel.setText(_translate('FindPersonWindow', 'Patronymic:'))
        self.birthdateLabel.setText(_translate('FindPersonWindow', 'Birthdate:'))
        self.countryLabel.setText(_translate('FindPersonWindow', 'Country:'))
        self.phoneNumberLabel.setText(_translate('FindPersonWindow', 'Phone number:'))
        self.emailLabel.setText(_translate('FindPersonWindow', 'E-mail:'))


    def select_image(self):
        file_dialog = QFileDialog()
        pictures_dir = QStandardPaths.writableLocation(
            QStandardPaths.StandardLocation.PicturesLocation)
        file_dialog.setDirectory(pictures_dir)

        image_path, _ = file_dialog.getOpenFileName(
            self, "Select Image", "", "Image Files (*.jpg *.png)")

        self.photoLineEdit.setText(image_path)

    def get_all_face_data(self):
        return self.session.query(self.FaceDataModel).all()

    def display_search_results(self):
        similar_face_person_ids = self.photo_handler.search_faces(self.photoLineEdit.text(),
                                                                   self.get_all_face_data())
        person = self.session.query(self.PersonsModel).filter_by(identifier=similar_face_person_ids[0]).first()
        self.firstNameLineEdit.setText(person.first_name)
        self.lastNameLineEdit.setText(person.last_name)
        self.patronymicLineEdit.setText(person.patronymic)
        self.birthdateDataEdit.setDate(person.birthdate)
        self.countryLineEdit.setText(person.country)
        self.phoneNumberLineEdit.setText(person.phone_num)
        self.emailLineEdit.setText(person.email)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    find_person_window = FindPersonWindow()
    find_person_window.show()

    sys.exit(app.exec())
