#!/usr/bin/python3
"""FileStorage"""
import json


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
                obj_dict = {key: obj.to_dict()}
            json.dump(obj_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    cls_name, obj_id = key.split('.')
                    inst_cls = eval(cls_name)(**value)
                    self.__objects[key] = inst_cls
        except FileNotFoundError:
            pass
