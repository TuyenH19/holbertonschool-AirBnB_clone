#!/usr/bin/python3
"""class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User"""
    def __init__(self, *args, **kwars):
        super(). __init__(*args, **kwars)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
