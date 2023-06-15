from baseModel import BaseModel
from sqlalchemy import Column, String, Date, LargeBinary
from sqlalchemy.orm import relationship


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
