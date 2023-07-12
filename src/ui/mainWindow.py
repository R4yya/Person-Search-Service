from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow
from ui.addRecordWindow import AddRecordWindow
from ui.findPersonWindow import FindPersonWindow


class MainWindow(QMainWindow):
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
        self.setObjectName('MainWindow')

        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName('central_widget')
        self.setCentralWidget(self.central_widget)

        self.gridLayout = QtWidgets.QGridLayout(self.central_widget)
        self.gridLayout.setObjectName('gridLayout_edits')

        self.findButton = QtWidgets.QPushButton(self.central_widget)
        self.findButton.setObjectName('findButton')
        self.findButton.clicked.connect(self.raise_find_person_window)
        self.gridLayout.addWidget(self.findButton, 0, 0, 1, 1)

        self.addRecordButton = QtWidgets.QPushButton(self.central_widget)
        self.addRecordButton.setObjectName('addRecordButton')
        self.addRecordButton.clicked.connect(self.raise_add_record_window)
        self.gridLayout.addWidget(self.addRecordButton, 1, 0, 1, 1)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate

        self.setWindowTitle(_translate('MainWindow', 'Main'))

        self.findButton.setText(_translate('MainWindow', 'Find'))
        self.addRecordButton.setText(_translate('MainWindow', 'Add new record'))

    def raise_find_person_window(self):
        self.find_person_window = FindPersonWindow(self.session,
                                                   self.PersonsModel,
                                                   self.FaceDataModel,
                                                   self.photo_handler)
        self.find_person_window.show()

    def raise_add_record_window(self):
        # self.hide()

        self.add_record_window = AddRecordWindow(self.session,
                                                 self.PersonsModel,
                                                 self.FaceDataModel,
                                                 self.photo_handler)
        self.add_record_window.show()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
