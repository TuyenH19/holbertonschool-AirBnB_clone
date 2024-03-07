#!/usr/bin/python3
"""Class user that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """define class user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
