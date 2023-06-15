from baseModel import BaseModel
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import ARRAY, REAL
from sqlalchemy.orm import relationship


class FaceDataModel(BaseModel):
    __tablename__ = 'face_data'

    person_id = Column(Integer, ForeignKey('persons.identifier'),
                       nullable=False)
    encoding = Column(ARRAY(REAL, dimensions=2), nullable=False)
    location = Column(ARRAY(Integer, dimensions=2, as_tuple=True),
                      nullable=False)

    person = relationship('PersonsModel', back_populates='face_encodings')
