#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
                "City",
                backref="state",
                cascade="all, delete-orphan")

    else:
        @property
        def cities(self):
            """
            Returns City objects with state_id equal to
            State.id

            """
            from models import storage
            city_list = []
            for city_id, city in storage.all(City):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
