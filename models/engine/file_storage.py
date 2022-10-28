#!/usr/bin/python3
"""
class file storage
"""
import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Class for handling the storage of the data
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Method for returning all files in storage.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Method for addingg new data in dtorage
        """
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """
        Methos for saving changes in file storage
        """
        first_dict = {}
        for key, val in FileStorage.__objects.items():
            if val:
                first_dict[key] = val.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(first_dict, f)

    def reload(self):
        """
        Method for reloading the class
        """
        a = 'BaseModel'
        b = 'User'
        c = 'Place'
        d = 'State'
        e = 'City'
        f = 'Amenity'
        g = 'Review'

        a1 = BaseModel
        b1 = User
        c1 = Place
        d1 = State
        e1 = City
        f1 = Amenity
        g1 = Review

        my_dict = {a: a1, b: b1, c: c1, d: d1, e: e1, f: f1, g: g1}

        if os.path.isfile(FileStorage.__file_path):
            with ope(FileStorage.__file_path, 'r', encoding='utf-8') as q:
                other_dict = json.load(q.read())
                for key, val in other_dict.items():
                    self.new(my_dict[val['__class__']](**val))
