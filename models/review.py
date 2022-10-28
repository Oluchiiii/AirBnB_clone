#!/usr/bin/python3
"""
Model review
Handles reviews made on the property by
a user
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    inheritated class Review from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
