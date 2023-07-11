from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseOperator(object):
    def __init__(self):
        pass

    def setup_session(self, db_uri):
        self.engine = create_engine(db_uri)
        self.session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.session()
