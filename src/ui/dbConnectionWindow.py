from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow
from ui.mainWindow import MainWindow
from json import dump, load
from os.path import dirname, join as os_join


class DbConnectionWindow(QMainWindow):
    def __init__(self,
                 DatabaseSession,
                 PersonsModel,
                 FaceDataModel,
                 PhotoHandler,
                 parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.retranslate_ui()
        self.read_from_json()
        self.db_session = DatabaseSession
        self.PersonsModel = PersonsModel
        self.FaceDataModel = FaceDataModel
        self.photo_handler = PhotoHandler

    def setup_ui(self):
        self.setObjectName('DbConnectionWindow')
        self.setFixedSize(320, 210)

        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName('central_widget')
        self.setCentralWidget(self.central_widget)

        self.gridLayout = QtWidgets.QGridLayout(self.central_widget)
        self.gridLayout.setObjectName('gridLayout_edits')

        self.usernameLabel = QtWidgets.QLabel(self.central_widget)
        self.usernameLabel.setObjectName('usernameLabel')
        self.gridLayout.addWidget(self.usernameLabel, 0, 0, 1, 1)

        self.passLabel = QtWidgets.QLabel(self.central_widget)
        self.passLabel.setObjectName('passLabel')
        self.gridLayout.addWidget(self.passLabel, 1, 0, 1, 1)

        self.hostLabel = QtWidgets.QLabel(self.central_widget)
        self.hostLabel.setObjectName('hostLabel')
        self.gridLayout.addWidget(self.hostLabel, 2, 0, 1, 1)

        self.databaseLabel = QtWidgets.QLabel(self.central_widget)
        self.databaseLabel.setObjectName('databaseLabel')
        self.gridLayout.addWidget(self.databaseLabel, 3, 0, 1, 1)

        self.usernameLineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.usernameLineEdit.setObjectName('usernameLineEdit')
        self.gridLayout.addWidget(self.usernameLineEdit, 0, 1, 1, 1)

        self.passLineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.passLineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.passLineEdit.setObjectName('passLineEdit')
        self.gridLayout.addWidget(self.passLineEdit, 1, 1, 1, 1)

        self.hostLineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.hostLineEdit.setObjectName('hostLineEdit')
        self.gridLayout.addWidget(self.hostLineEdit, 2, 1, 1, 1)

        self.databaseLineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.databaseLineEdit.setObjectName('databaseLineEdit')
        self.gridLayout.addWidget(self.databaseLineEdit, 3, 1, 1, 1)

        self.checkBox = QtWidgets.QCheckBox(self.central_widget)
        self.checkBox.setObjectName('checkBox')
        self.gridLayout.addWidget(self.checkBox, 4, 0, 1, 2)

        self.clearButton = QtWidgets.QPushButton(self.central_widget)
        self.clearButton.setObjectName('clearButton')
        self.clearButton.clicked.connect(self.clear_edits)
        self.gridLayout.addWidget(self.clearButton, 5, 2, 1, 1)

        self.connectButton = QtWidgets.QPushButton(self.central_widget)
        self.connectButton.setObjectName('connectButton')
        self.connectButton.clicked.connect(self.connect_to_db)
        self.gridLayout.addWidget(self.connectButton, 6, 2, 1, 1)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate

        self.setWindowTitle(_translate('DbConnectionWindow', 'Connect to database'))

        self.usernameLabel.setText(_translate('DbConnectionWindow', 'Unsername:'))
        self.passLabel.setText(_translate('DbConnectionWindow', 'Password:'))
        self.hostLabel.setText(_translate('DbConnectionWindow', 'host:'))
        self.databaseLabel.setText(_translate('DbConnectionWindow', 'Database:'))
        self.checkBox.setText(_translate('DbConnectionWindow', 'Remember me'))
        self.connectButton.setText(_translate('DbConnectionWindow', 'Connect'))
        self.clearButton.setText(_translate('DbConnectionWindow', 'Clear'))

    def clear_edits(self):
        self.usernameLineEdit.clear()
        self.passLineEdit.clear()
        self.hostLineEdit.clear()
        self.databaseLineEdit.clear()

    def get_json_path(self):
        project_path = "\\".join(dirname(__file__).split("\\")[:-1])
        json_path = f'{project_path}\\saved_data_json'
        return json_path

    def remember_me(self):
        if self.checkBox.isChecked():
            self.save_to_json()

    def save_to_json(self):
        data = {
            'username': self.usernameLineEdit.text(),
            'password': self.passLineEdit.text(),
            'host': self.hostLineEdit.text(),
            'database': self.databaseLineEdit.text()
        }

        json_path = self.get_json_path()

        with open(os_join(json_path, 'connection_pref.json'), 'w') as file:
            dump(data, file)

    def read_from_json(self):
        json_path = self.get_json_path()

        with open(os_join(json_path, 'connection_pref.json'), 'r') as file:
            connection_pref_dict = load(file)

        self.usernameLineEdit.setText(connection_pref_dict['username'])
        self.passLineEdit.setText(connection_pref_dict['password'])
        self.hostLineEdit.setText(connection_pref_dict['host'])
        self.databaseLineEdit.setText(connection_pref_dict['database'])

    def get_uri(self):
        username = self.usernameLineEdit.text()
        password = self.passLineEdit.text()
        host = self.hostLineEdit.text()
        database = self.databaseLineEdit.text()

        return f'postgresql://{username}:{password}@localhost:{host}/{database}'

    def raise_main_window(self,
                          session,
                          PersonsModel,
                          FaceDataModel,
                          PhotoHandler):
        self.hide()
        self.main_window = MainWindow(session,
                                      PersonsModel,
                                      FaceDataModel,
                                      PhotoHandler)
        self.main_window.show()

    def connect_to_db(self):
        self.remember_me()

        uri = self.get_uri()
        self.db_session.setup_session(uri)
        session = self.db_session.get_session()

        self.raise_main_window(session,
                               self.PersonsModel,
                               self.FaceDataModel,
                               self.photo_handler)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    db_connection_window = DbConnectionWindow()
    db_connection_window.show()

    sys.exit(app.exec())
