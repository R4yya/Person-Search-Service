from src.databaseSession import DatabaseSession
from src.personsModel import PersonsModel
from convert_image_to_bytes import get_bytes_from_file

# Создаем экземпляр класса DatabaseSession
db_session = DatabaseSession('your_db_uri')

# Получаем сессию из DatabaseSession
session = db_session.get_session()

# Создаем образцы данных для заполнения таблицы
samples = [
    {
        'first_name': 'Pavel',
        'last_name': 'Durov',
        'patronymic': 'Valeryevich',
        'birthdate': '1994-10-10',
        'country': 'Russia',
        'phone_num': '+79155590507',
        'email': 'durov@mail.com',
        'photo': get_bytes_from_file('durov.bin')
    }
]

# Заполняем таблицу с использованием модели и сессии
for sample in samples:
    person = PersonsModel(**sample)
    session.add(person)

# Выполняем коммит, чтобы сохранить данные в базе данных
session.commit()

# Закрываем сессию
session.close()
