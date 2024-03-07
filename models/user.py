#!/usr/bin/python3
"""class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User"""
    def user(self, *args, **kwars):
            def __init__(self):
                self.email = ""
                self.password = ""
                self.first_name = ""
                self.last_name = ""
                