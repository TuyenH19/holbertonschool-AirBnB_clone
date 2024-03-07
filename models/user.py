#!/usr/bin/python3
"""class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """Create class User that inherits from BaseModel"""
    def user(self, *args, **kwargs):
        email = ""
        password = ""
        first_name = ""
        last_name = ""
