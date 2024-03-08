#!/usr/bin/python3
"""FileStorage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """Create class FileStorag for representing an abstracted storage engine"""
    __file_path = "file.json"  # path to the JSON file (ex: file.json)
    __objects = {}  # dictionary - store all objects by <class name>.id

    def all(self):
        """"Return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, 'w') as file:
            obj_dict = {}
            for key, obj in self.__objects.items():
                obj_dict[key] = obj.to_dict()
            json.dump(obj_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "Review": Review,
            "Place": Place,
            "City": City,
            "Amenity": Amenity,
        }

        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
                for obj_id, obj in data.items():
                    cls_name = obj['__class__']
                    if cls_name in class_dict:
                        cls = class_dict[cls_name]
                        self.__objects[obj_id] = cls(**obj)
        except FileNotFoundError:
            pass
