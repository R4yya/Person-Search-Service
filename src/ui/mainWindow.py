from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, session, PersonsModel, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.retranslate_ui()
        self.session = session
        self.persons = PersonsModel

    def setup_ui(self):
        self.setObjectName('MainWindow')
        self.setFixedSize(800, 600)

        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName('central_widget')
        self.setCentralWidget(self.central_widget)

        self.gridLayout = QtWidgets.QGridLayout(self.central_widget)
        self.gridLayout.setObjectName('gridLayout_edits')

        self.printButton = QtWidgets.QPushButton(self.central_widget)
        self.printButton.setObjectName('printButton')
        self.printButton.clicked.connect(self.print_all)
        self.gridLayout.addWidget(self.printButton, 0, 0, 1, 1)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate

        self.setWindowTitle(_translate('MainWindow', 'Main'))

        self.printButton.setText(_translate('MainWindow', 'Print'))

    def print_all(self):
        persons = self.session.query(self.persons).all()
        for person in persons:
            print(person.first_name)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
