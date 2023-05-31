from src.databaseSession import DatabaseSession
from src.personsModel import PersonsModel
from convert_image_to_bytes import get_bytes_from_file


# Set URI
username = input('username: ')
password = input('password: ')
uri = f'postgresql://{username}:{password}@localhost:5432/person_search'

# Create an instance of the DatabaseSession
db_session = DatabaseSession(uri)

# Get session from DatabaseSession
session = db_session.get_session()

# Create data samples to fill table
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

# Fill table using model and session
for sample in samples:
    person = PersonsModel(**sample)
    session.add(person)

# Perform a commit to save the data in database
session.commit()

# End session
session.close()
