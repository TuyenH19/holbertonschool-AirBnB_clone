#!/usr/bin/python3
"""tests for base model"""
import unittest
from models import storage
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        """Test initialization of the BaseModel"""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        """Test __str__ method"""
        model = BaseModel()
        self.assertIn(model.__class__.__name__, str(model))
        self.assertIn(model.id, str(model))
        self.assertIn(str(model.__dict__), str(model))

    def test_save(self):
        """Test save method"""
        model = BaseModel()
        previous_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(previous_updated_at, model.updated_at)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())

    def test_to_dict(self):
        """Test to_dict method"""
        md = BaseModel()
        md_dict = md.to_dict()
        self.assertIsInstance(md_dict, dict)
        self.assertIn('__class__', md_dict)
        self.assertEqual(md_dict['__class__'], 'BaseModel')
        self.assertIn('id', md_dict)
        self.assertIn('created_at', md_dict)
        self.assertIn('updated_at', md_dict)
        self.assertEqual(md_dict['id'], md.id)
        self.assertEqual(md_dict['created_at'], md.created_at.isoformat())
        self.assertEqual(md_dict['updated_at'], md.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
