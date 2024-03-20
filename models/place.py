#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from models.base_model import BaseModel, Base
from os import getenv

association_table = Table('place_amenity',
                          Base.metadata,
                          Column('place_id',
                                 ForeignKey('places.id'),
                                 nullable=False),
                          Column('amenity_id'
                                 ForeignKey('amenities.id'),
                                 nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1204), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
                'Review',
                backref='place',
                cascade='all, delete-orphan')
        amenities = relationship('Amenity',
                                 secondary=association_table,
                                 viewonly=False,
                                 overlaps='places')
