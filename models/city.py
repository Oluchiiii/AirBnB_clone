#!/usr/bin/python3

"""
Model city
Class for city the propery is
situated
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class inherits from BaseModel
    """
    name = ""
    state_id = ""
