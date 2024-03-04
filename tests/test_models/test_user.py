#!/usr/bin/python3
import unittest
from models import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        """Test the initialization of BaseModel"""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_str(self):
        """Test the __str__ method"""
        model = BaseModel()
        expected_output = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_output)

    def test_save(self):
        """Test the save method"""
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'],
                         model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         model.updated_at.isoformat())

    if __name__ == '__main__':
        unittest.main()
