#!/usr/bin/python3
"""class user"""
from models.base_model import BaseModel


class User(BaseModel):
<<<<<<< HEAD
    """Create class User that inherits from BaseModel"""
    def user(self, *args, **kwargs):
        email = ""
        password = ""
        first_name = ""
        last_name = ""
=======
    def user(self, *args, **kwars):
            def __init__(self):
                self.email = ""
                self.password = ""
                self.first_name = ""
                self.last_name = ""
                
            
>>>>>>> a9bae9209cae94d4abdf1102cdb53da56f6ac28a
