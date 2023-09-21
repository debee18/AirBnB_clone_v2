#!/usr/bin/python3
"""
File Storage class
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """
    File Storage class
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_dict = {}
        for key, value in FileStorage.__objects.items():
            json_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(json_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                json_dict = json.load(f)

            for key, value in json_dict.items():
                cls_name, obj_id = key.split('.')
                cls = eval(cls_name)
                obj = cls(**value)
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass

    def close(self):
        """Calls the reload() method for deserializing the JSON file to objects"""
        self.reload()

