from PyQt6 import QtWidgets
from os.path import join as os_join, dirname
import sys
from ui.dbConnectionWindow import DbConnectionWindow
from db_operator.databaseSession import DatabaseSession
from models.tablesModels import PersonsModel, FaceDataModel
from photo_handler.photoHandler import PhotoHandler


def update_sys_path():

    folders = ['db_operator', 'models', 'photo_handler',
               'saved_data_json', 'ui', 'utils']

    for folder in folders:
        fpath = os_join('\\'.join(dirname(__file__).split('\\')[:-1]), folder)
        sys.path.append(fpath)


if __name__ == '__main__':
    update_sys_path()

    app = QtWidgets.QApplication(sys.argv)

    db_connection_window = DbConnectionWindow(
        DatabaseSession(),
        PersonsModel,
        FaceDataModel,
        PhotoHandler())
    db_connection_window.show()

    sys.exit(app.exec())
