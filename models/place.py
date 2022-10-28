#!/usr/bin/python3
"""
Model place
Class place for handling property
information such as name, city, # of guest,
latitude and longitude of property
"""

from models.base_model import BaseModel


class Place(BaseModel):
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
