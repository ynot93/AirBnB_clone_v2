#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
#from sqlalchemy import Column, String, ForeignKey
#from sqlalchemy.orm import relationship
#from sqlalchemy.ext.declarative import declarative_base

#Base = declarative_base()


class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""
