from src.models.databaseSession import DatabaseSession
from src.models.personsModel import PersonsModel
from convert_image_to_bytes import get_bytes_from_file


def initialize_database_session():
    # Get URI
    username = input('username: ')
    password = input('password: ')
    uri = f'postgresql://{username}:{password}@localhost:5432/person_search'

    # Create an instance of the DatabaseSession
    db_connection = DatabaseSession(uri)

    # Get session from DatabaseSession
    session = db_connection.get_session()

    return session


def fill_persons_table(samples):
    # Fill table using model and session
    for sample in samples:
        person = PersonsModel(**sample)
        session.add(person)

    # Perform a commit to save the data in database
    session.commit()

    # End session
    session.close()


if __name__ == '__main__':
    session = initialize_database_session()

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
            'first_name': 'William',
            'last_name': 'Gates',
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

    fill_persons_table(samples)
