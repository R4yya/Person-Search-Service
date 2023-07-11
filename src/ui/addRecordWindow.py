from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QFileDialog
from PyQt6.QtCore import QStandardPaths


class AddRecordWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.retranslate_ui()

    def setup_ui(self):
        self.setObjectName('MainWindow')
        self.setFixedSize(400, 270)

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

        self.firstNameLineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.firstNameLineEdit.setObjectName('firstNameLineEdit')
        self.gridLayout.addWidget(self.firstNameLineEdit, 0, 1, 1, 2)

        self.lastNameLineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.lastNameLineEdit.setObjectName('lastNameLineEdit')
        self.gridLayout.addWidget(self.lastNameLineEdit, 1, 1, 1, 2)

        self.patronymicLineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.patronymicLineEdit.setObjectName('patronymicLineEdit')
        self.gridLayout.addWidget(self.patronymicLineEdit, 2, 1, 1, 2)

        self.birthdateLineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.birthdateLineEdit.setObjectName('birthdateLineEdit')
        self.gridLayout.addWidget(self.birthdateLineEdit, 3, 1, 1, 2)

        self.countryLineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.countryLineEdit.setObjectName('countryLineEdit')
        self.gridLayout.addWidget(self.countryLineEdit, 4, 1, 1, 2)

        self.phoneNumberLineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.phoneNumberLineEdit.setObjectName('phoneNumberLineEdit')
        self.gridLayout.addWidget(self.phoneNumberLineEdit, 5, 1, 1, 2)

        self.emailLineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.emailLineEdit.setObjectName('emailLineEdit')
        self.gridLayout.addWidget(self.emailLineEdit, 6, 1, 1, 2)

        self.photoLineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.photoLineEdit.setObjectName('photoLineEdit')
        self.gridLayout.addWidget(self.photoLineEdit, 7, 0, 1, 2)

        self.selectPhotoButton = QtWidgets.QPushButton(self.central_widget)
        self.selectPhotoButton.setObjectName('selectPhotoButton')
        self.selectPhotoButton.clicked.connect(self.select_image)
        self.gridLayout.addWidget(self.selectPhotoButton, 7, 2, 1, 1)

        self.addRecordButton = QtWidgets.QPushButton(self.central_widget)
        self.addRecordButton.setObjectName('addRecordButton')
        # self.addRecordButton.clicked.connect()
        self.gridLayout.addWidget(self.addRecordButton, 8, 3, 1, 1)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate

        self.setWindowTitle(_translate('MainWindow', 'Add record'))

        self.firstNameLabel.setText(_translate('MainWindow', 'First name:'))
        self.lastNameLabel.setText(_translate('MainWindow', 'Last name:'))
        self.patronymicLabel.setText(_translate('MainWindow', 'Patronymic:'))
        self.birthdateLabel.setText(_translate('MainWindow', 'Birthdate:'))
        self.countryLabel.setText(_translate('MainWindow', 'Country:'))
        self.phoneNumberLabel.setText(_translate('MainWindow', 'Phone number:'))
        self.emailLabel.setText(_translate('MainWindow', 'E-mail:'))
        self.selectPhotoButton.setText(_translate('MainWindow', 'Select photo'))
        self.addRecordButton.setText(_translate('MainWindow', 'Add'))

    def select_image(self):
        file_dialog = QFileDialog()
        pictures_dir = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.PicturesLocation)
        file_dialog.setDirectory(pictures_dir)
        image_path, _ = file_dialog.getOpenFileName(
            self, "Select Image", "", "Image Files (*.jpg *.png)")
        self.photoLineEdit.setText(image_path)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    add_record_window = AddRecordWindow()
    add_record_window.show()

    sys.exit(app.exec())
