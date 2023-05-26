from sqlalchemy import Column, Integer, String, Date, LargeBinary
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PersonsModel(Base):
    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    patronymic = Column(String(50))
    birthdate = Column(Date, nullable=False)
    country = Column(String(100), nullable=False)
    phone_num = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False)
    photo = Column(LargeBinary, nullable=False)
