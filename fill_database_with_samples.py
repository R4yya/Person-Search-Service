from src.databaseSession import DatabaseSession
from src.personsModel import PersonsModel
from convert_image_to_bytes import get_bytes_from_file

# Универсальный идентификатор ресурса
username = input('username: ')
password = input('password: ')
uri = f'postgresql://{username}:{password}@localhost:5432/person_search'

# Создаем экземпляр класса DatabaseSession
db_session = DatabaseSession(uri)

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
    },
    {
        'first_name': 'Gates',
        'last_name': 'William',
        'patronymic': None,
        'birthdate': '1955-10-28',
        'country': 'USA',
        'phone_num': '+18332691066',
        'email': 'gates@mail.com',
        'photo': get_bytes_from_file('gates.bin')
    },
    {
        'first_name': 'Mark',
        'last_name': 'Zuckerberg',
        'patronymic': None,
        'birthdate': '1984-05-14',
        'country': 'USA',
        'phone_num': '+18332626819',
        'email': 'zuckerberg@mail.com',
        'photo': get_bytes_from_file('zuckerberg.bin')
    },
]

# Заполняем таблицу с использованием модели и сессии
for sample in samples:
    person = PersonsModel(**sample)
    session.add(person)

# Выполняем коммит, чтобы сохранить данные в базе данных
session.commit()

# Закрываем сессию
session.close()
