#!/usr/bin/pytho3
"""
Module base_model
Contains a class "BaseModel" that defines all
common attributes/methods for other classes.
"""


import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Defines all common attributes for
    other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializing the public attribute
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.item():
                if key == "created_at" or key == "update_at":
                    time_format = "%Y-%m-%dT%H:%M:%S.%f"
                    value = datetime.strptime(kwargs[key], time_format)
                    if key != "__class__":
                        setattr(self, key, value)

    def __str__(self):
        """Prints something in specific format"""
        ClassName = self.__class__.__name__
        return ("[{}] ({}) {}".format(ClassName, self.id, self.__dict__))

    def save(self):
        """
        Updates public attribute "updated_at"
        to current datetime.
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns dict with all keys/values of __dict__
        """

        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        my_dict = dict(self.__dict__)
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.strftime(time_format)
        my_dict['updated_at'] = self.updated_at.strftime(time_format)

        return my_dict
