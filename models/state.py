#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship
from sqlalcehmy import Column, String
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            from models import storage
            file_cities = storage.all(City).values()
            return [city for city in file_cities if city.state_id == self.id]
