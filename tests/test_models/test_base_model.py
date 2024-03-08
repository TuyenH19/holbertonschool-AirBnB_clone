#!/usr/bin/python3
"""unittest for base_model"""


import unittest
from models.base_model import BaseModel
from datetime import datetime
from io import StringIO

class TestBaseModel(unittest.TestCase):

    def setUP(self):
        """Set up for each test"""
        self.bm = BaseModel()







if __name__ == '__main__':
    unittest.main()
