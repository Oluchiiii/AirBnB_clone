#!/usr/bin/python3

"""
Module test_base_model
Has the test for the BaseModel class
"""


import unittest
import uuid
from datetime import datetime as dt
#from models import storage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Testing if the BaseModel functions properly
    """

    def test_methods_and_attributes():
        """
        Test if moethod is in base_model.
        """
        self.AssertTrue(hasattr(BaseModel(), "__str__"))
        self.AssertTrue(hasattr(BaseModel(), "save"))
        self.AssertTrue(hasattr(BaseModel(), "to_dict"))
        self.AssertTrue(hasattr(BaseModel(), "created_at"))
        self.AssertTrue(hasattr(BaseModel(), "updated_at"))

if __name__ == "__main__":
    unittest.main()
