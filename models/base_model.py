#!/usr/bin/python3
"""
Module base_model
Contains a class "BaseModel" that defines all
common attributes/methods for other classes.
"""


import uuid
from datetime import datetime as dt
from models import storage

class BaseModel:
    """
    Defines all common attributes for
    other classes.
    """

    def __init__(self, *args, **kwargs):
       "" "Initializing the publick attribute"""

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            storage.new(self)
        else:
            for key, value in kwargs.item():
                if key == "vreated_at" or key == "update_at":
                    value = dt.strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """Prints something in specific format"""
        ClassName = self.__class__.__name__
        print("[{}] ({}) {}".format(ClassName, self.id, self.__dict__))

    def save(self):
        """
        Updates public attribute "updated_at"
        to current datetime.
        """

        self.updated_at = dt.now()
        storage.save()

    def to_dict(self):
        """
        Returns dict with all keys/values of __dict__
        """

        my_dict = {key: value for key, value in self.__dict__.item()}
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()

        return my_dict
