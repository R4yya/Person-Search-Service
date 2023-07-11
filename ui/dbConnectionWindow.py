from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow
from json import dump, load
from convert_image_to_bytes import get_project_path
from os.path import os_join


class DbConnectionWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName('MainWindow')
        self.setFixedSize(330, 200)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName('centralwidget')
        self.setCentralWidget(self.centralwidget)

        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 291, 161))
        self.widget.setObjectName('widget')

        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName('gridLayout')

        self.usernameLabel = QtWidgets.QLabel(parent=self.widget)
        self.usernameLabel.setObjectName('usernameLabel')
        self.gridLayout.addWidget(self.usernameLabel, 0, 0, 1, 1)

        self.passLabel = QtWidgets.QLabel(parent=self.widget)
        self.passLabel.setObjectName('passLabel')
        self.gridLayout.addWidget(self.passLabel, 1, 0, 1, 1)

        self.portLabel = QtWidgets.QLabel(parent=self.widget)
        self.portLabel.setObjectName('portLabel')
        self.gridLayout.addWidget(self.portLabel, 2, 0, 1, 1)

        self.databaseLabel = QtWidgets.QLabel(parent=self.widget)
        self.databaseLabel.setObjectName('databaseLabel')
        self.gridLayout.addWidget(self.databaseLabel, 3, 0, 1, 1)

        self.usernameLineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.usernameLineEdit.setObjectName('usernameLineEdit')
        self.gridLayout.addWidget(self.usernameLineEdit, 0, 1, 1, 1)

        self.passLineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.passLineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.passLineEdit.setObjectName('passLineEdit')
        self.gridLayout.addWidget(self.passLineEdit, 1, 1, 1, 1)

        self.portLineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.portLineEdit.setObjectName('portLineEdit')
        self.gridLayout.addWidget(self.portLineEdit, 2, 1, 1, 1)

        self.databaseLineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.databaseLineEdit.setObjectName('databaseLineEdit')
        self.gridLayout.addWidget(self.databaseLineEdit, 3, 1, 1, 1)

        self.checkBox = QtWidgets.QCheckBox(parent=self.widget)
        self.checkBox.setObjectName('checkBox')
        self.gridLayout.addWidget(self.checkBox, 4, 0, 1, 2)

        self.connectButton = QtWidgets.QPushButton(parent=self.widget)
        self.connectButton.setObjectName('connectButton')
        self.connectButton.clicked.connect(self.remember_me)
        self.gridLayout.addWidget(self.connectButton, 5, 2, 1, 1)

        self.retranslate_ui()

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate(
            'MainWindow', 'Connect to database'))

        self.usernameLabel.setText(_translate('MainWindow', 'Unsername:'))
        self.passLabel.setText(_translate('MainWindow', 'Password:'))
        self.portLabel.setText(_translate('MainWindow', 'Port:'))
        self.databaseLabel.setText(_translate('MainWindow', 'Database:'))
        self.checkBox.setText(_translate('MainWindow', 'Remember me'))
        self.connectButton.setText(_translate('MainWindow', 'Connect'))

    def remember_me(self):
        if self.checkBox.isChecked():
            self.save_to_json()

    def save_to_json(self):
        data = {
            'username': self.usernameLineEdit.text(),
            'password': self.upasswordLineEdit.text(),
            'port': self.portLineEdit.text(),
            'database': self.databaseLineEdit.text()
        }

        with open('connection_pref.json', 'w') as file:
            dump(data, file)

    def read_from_json(self):
        with open(os_join(f'{get_project_path()}\\img_bytes', 'connection_pref.json'), 'w') as file:
            connection_pref_dict = load(file)

        self.usernameLineEdit.setText(connection_pref_dict['username'])
        self.upasswordLineEdit.setText(connection_pref_dict['password'])
        self.portLineEdit.setText(connection_pref_dict['port'])
        self.databaseLineEdit.setText(connection_pref_dict['database'])

    def get_uri(self):
        pass


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    db_connection_window = DbConnectionWindow()
    db_connection_window.show()

    sys.exit(app.exec())
