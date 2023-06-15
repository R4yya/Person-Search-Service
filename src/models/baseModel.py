from sqlalchemy import Column, Integer
from sqlalchemy.orm.declarative import DeclarativeBase


class BaseModel(DeclarativeBase):
    identifier = Column(Integer, primary_key=True)
