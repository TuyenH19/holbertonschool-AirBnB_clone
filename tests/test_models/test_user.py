import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User


class TestBaseModel(unittest.TestCase):
    """TestBaseModel with unittest"""
    def test_user_to_dict_method(self):
        """Test to_dict method"""
        user_instance = User()
        user_dict = user_instance.to_dict()

        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], "")
        self.assertEqual(user_dict['password'], "")
        self.assertEqual(user_dict['first_name'], "")
        self.assertEqual(user_dict['last_name'], "")

    if __name__ == '__main__':
        unittest.main()
        