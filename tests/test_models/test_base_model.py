#!/usr/bin/python3

"""
Module test_base_model
Has the test for the BaseModel class
"""


import unittest
from uuid import UUID
from datetime import datetime
from models.base_model import BaseModel
from models import storage

class TestBaseModel(unittest.TestCase):
    """
    Testing if the BaseModel functions properly
    """

    def test_normal_cases_base_model(self):
        """
        Test for normal case use of base model
        """
        my_object = BaseModel()
        my_object.name = "Kuvukiland"
        my_object.my_number = 24
        my_object.save()
        my_object_dict = my_object.to_dict()

        self.AssertEqual(my_object.__class__.__name__, "BaseModel")
        self.AssertEqual(my_object.name, "kuvukiland")
        self.AssertEqual(my_object.my_number, 24)
        self.AssertEqual(isinstance(my_object.created_at, datetime), True)
        self.AssertEqual(isinstance(my_object.updated_at, datetime), True)
        self.AssertEqual(type(my_object.__dict__), dict)

if __name__ == "__main__":
    unittest.main()
