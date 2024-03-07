#!/usr/bin/python3
"""BaseModel"""


import uuid
import json
from models.engine.file_storage import FileStorage
<<<<<<< HEAD
from models import storage
=======
>>>>>>> a9bae9209cae94d4abdf1102cdb53da56f6ac28a
from datetime import datetime
from models import storage


class BaseModel:
    """create BaseModel"""
<<<<<<< HEAD
    tformat = "%Y-%m-%dT%H:%M:%S.%f"
    __nb_objects = 0
=======
    __nb_objects = 0
    tformat = "%Y-%m-%dT%H:%M:%S.%f"
    storage = None
>>>>>>> a9bae9209cae94d4abdf1102cdb53da56f6ac28a

    def __init__(self, *args, **kwargs):
        """initialized"""
        if kwargs:
            for key, value in kwargs.items():  # check key, value
                if key != "__class__":  # different of__class__
                    if key in ['created_at', 'updated_at']:
<<<<<<< HEAD
                       setattr(self, key, datetime.strptime(value, BaseModel.tformat))#if key is 'created_at' or 'updated_at', we convert the value of the string to object 
=======
                        setattr(self, key, datetime.strptime(value, BaseModel.tformat))  # noqa # # if key is 'created_at' or 'updated_at', w
>>>>>>> a9bae9209cae94d4abdf1102cdb53da56f6ac28a
                    else:
                        setattr(self, key, value)  # for other key and value
        else:
            BaseModel.__nb_objects += 1
<<<<<<< HEAD
            self.id = str(uuid.uuid4())#ID unique
            self.created_at = datetime.now()#Create
            self.updated_at = datetime.now()#update
=======
            self.id = str(uuid.uuid4())  # ID unique
            self.created_at = datetime.now()  # Create
            self.updated_at = datetime.now()  # update
            storage.new(self)
>>>>>>> a9bae9209cae94d4abdf1102cdb53da56f6ac28a

    def __str__(self):
        """Print class, ID, Dict"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update instance with the date and hour"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """return dict"""
        nw_dict = self.__dict__.copy()
        nw_dict['__class__'] = self.__class__.__name__
        nw_dict['created_at'] = self.created_at.isoformat()
        nw_dict['updated_at'] = self.updated_at.isoformat()
        return nw_dict
