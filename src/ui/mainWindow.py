from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow
from ui.addRecordWindow import AddRecordWindow


class MainWindow(QMainWindow):
    def __init__(self,
                 session,
                 PersonsModel,
                 parent=None):
        super().__init__(parent)
        self.session = session
        self.persons = PersonsModel
        self.setup_ui()
        self.retranslate_ui()

    def setup_ui(self):
        self.setObjectName('MainWindow')

        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName('central_widget')
        self.setCentralWidget(self.central_widget)

        self.gridLayout = QtWidgets.QGridLayout(self.central_widget)
        self.gridLayout.setObjectName('gridLayout_edits')

        self.printButton = QtWidgets.QPushButton(self.central_widget)
        self.printButton.setObjectName('printButton')
        self.printButton.clicked.connect(self.print_all)
        self.gridLayout.addWidget(self.printButton, 0, 0, 1, 1)

        self.addRecordButton = QtWidgets.QPushButton(self.central_widget)
        self.addRecordButton.setObjectName('addRecordButton')
        self.addRecordButton.clicked.connect(self.raise_add_record_window)
        self.gridLayout.addWidget(self.addRecordButton, 1, 0, 1, 1)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate

        self.setWindowTitle(_translate('MainWindow', 'Main'))

        self.printButton.setText(_translate('MainWindow', 'Print'))
        self.addRecordButton.setText( _translate('MainWindow', 'Add new record'))

    def print_all(self):
        persons = self.session.query(self.persons).all()
        for person in persons:
            print(person.first_name)

    def raise_add_record_window(self):
        self.hide()

        self.add_record_window = AddRecordWindow()
        self.add_record_window.show()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
