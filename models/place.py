#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """ Place class constructor """
        super().__init__(*args, **kwargs)
        from models.amenity import Amenity
    
        if getenv('HBNB_TYPE_STORAGE') == 'db':
            reviews = relationship('Review', backref='place', cascade='all, delete')
            amenities = relationship('Amenity', secondary='place_amenity', back_populates='places', viewonly=False)
        else:
            @property
            def reviews(self):
                """Getter attribute for reviews in File Storage"""
                from models import storage
            
                place_reviews = []
                all_reviews = storage.all(Review)

                for review in all_reviews.values():
                    if review.place_id == self.id:
                        place_reviews.append(review)
                return place_reviews

            @property
            def amenities(self):
                """Getter methods for amenities in File Storage"""
                from models import storage

                place_amenities = []
                all_amenities = storage.all(Amenity)

                for amenity in all_amenities.values():
                    if amenity.id in self.amenity_ids:
                        place_amenities.append(ammenity)
                return place_amenities

            @amenities.setter
            def amenities(self, amenity):
                """Setter method for amenities in File Storage"""
                if isinstance(amenity, Amenity):
                    if amenity.id not in self.amenity_ids:
                        self.amenity_ids.append(amenity.id)

