from sqlalchemy import Column, ForeignKey, Integer, String, Date, LargeBinary
from sqlalchemy.dialects.postgresql import ARRAY, REAL
from sqlalchemy.orm import relationship, DeclarativeBase


class BaseModel(DeclarativeBase):
    identifier = Column(Integer, primary_key=True)


class PersonsModel(BaseModel):
    __tablename__ = 'persons'

    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    patronymic = Column(String(50))
    birthdate = Column(Date, nullable=False)
    country = Column(String(100), nullable=False)
    phone_num = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False)
    photo = Column(LargeBinary, nullable=False)

    face_encodings = relationship('FaceDataModel', back_populates='person')


class FaceDataModel(BaseModel):
    __tablename__ = 'face_data'

    person_id = Column(Integer, ForeignKey(
        'persons.identifier'), nullable=False)
    encoding = Column(ARRAY(REAL), nullable=False)
    location = Column(ARRAY(Integer, as_tuple=True), nullable=False)

    person = relationship('PersonsModel', back_populates='face_encodings')
