from ..src.personSearchModel import PersonsModel
from ..src.databaseOperator import DatabaseSession

# Создаем экземпляр класса DatabaseSession
db_session = DatabaseSession('your_db_uri')

# Получаем сессию из DatabaseSession
session = db_session.get_session()

# Создаем образцы данных для заполнения таблицы
samples = [
    {
        'first_name': 'Павел',
        'last_name': 'Дуров',
        'patronymic': None,
        'birthdate': '1990-01-01',
        'country': 'USA',
        'phone_num': '123456789',
        'email': 'johndoe@example.com',
        'photo': b'\x01\x02\x03\x04'  # Пример байтов фотографии
    },
    # Добавьте другие образцы данных
]

# Заполняем таблицу с использованием модели и сессии
for sample in samples:
    person = PersonsModel(**sample)
    session.add(person)

# Выполняем коммит, чтобы сохранить данные в базе данных
session.commit()

# Закрываем сессию
session.close()
