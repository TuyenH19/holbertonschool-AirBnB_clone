#!/usr/bin/python3
"""test"""


import unittest
from models import BaseModel
def test_init(self):
    """Test the initialization of BaseModel"""
    model = BaseModel()
    self.assertIsInstance(model, BaseModel)
    self.assertTrue(hasattr(model, 'id'))
    self.assertTrue(hasattr(model, 'created_at'))
    self.assertTrue(hasattr(model, 'updated_at'))

if __name__ == '__main__':
    unittest.main()