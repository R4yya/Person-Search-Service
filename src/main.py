from PyQt6 import QtWidgets
from os.path import join as os_join, dirname
import sys
from ui.dbConnectionWindow import DbConnectionWindow
from db_operator.databaseOperator import DatabaseOperator
from models.tablesModels import PersonsModel


def update_sys_path():

    folders = ['db_operator', 'models', 'saved_data_json', 'ui', 'utils']

    for folder in folders:
        fpath = os_join('\\'.join(dirname(__file__).split('\\')[:-1]), folder)
        sys.path.append(fpath)


if __name__ == '__main__':
    update_sys_path()

    app = QtWidgets.QApplication(sys.argv)

    db_connection_window = DbConnectionWindow(
        DatabaseOperator(), PersonsModel)
    db_connection_window.show()

    sys.exit(app.exec())
