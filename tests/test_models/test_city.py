#!/usr/bin/python3
"""Unittests for base model class"""


import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
from uuid import UUID
from models import storage


class TestsAmenity(unittest.TestCase):
    """
    Tests the City class
    """
    obj = city()

    def setUp(self):
        """set initial"""
        name = ""
        state_id = ""

    def test_normal_cases_amenity(self):
        """ Normal cases """
        my_object = City()
        my_object.name = "Holbiland"
        my_object.my_number = 29
        my_object.save()
        my_object_dict = my_object.to_dict()

        self.assertEqual(my_object.name, "Holbiland")
        self.assertEqual(my_object.my_number, 29)
        self.assertEqual(my_object.__class__.__name__, "City")
        self.assertEqual(isinstance(my_object.created_at, datetime), True)
        self.assertEqual(isinstance(my_object.updated_at, datetime), True)
        self.assertEqual(type(my_object.__dict__), dict)

    def test_subclass(self):
        """test if class is subclass"""
        self.assertEqual(issubclass(City, BaseModel), True)

    def test_type(self):
        """tests for the typr of object"""
        self.assertEqual(type(self.obj.name), str)
        self.assertEqual(type(self.obj.name), str)

if __name__ == "__main__":
    unittest.main()
