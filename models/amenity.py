#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    place_amenities = Table(
            'place_amenity',
            Base.metadata)
