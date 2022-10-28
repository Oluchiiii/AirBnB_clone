#!/usr/bin/python3
"""
Model user
Handles the site's user information such
as email, name, surname, and password.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Class for user information
    """
    first_name = ""
    last_name = ""
    email = ""
    password = ""

    def __init__(self, *args, **kwargs):
        """
        Constructor for user
        """
        super().__init__(**kwargs)
