import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """TestBaseModel with unittest"""
    def setUp(self):
        """SetUp user for instances for testing"""
        self.user = User()
        
    def test_user_to_dict_method(self):
        """Test to_dict method"""
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertNotEqual(user_dict, self.user.__dict__)
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["id"], self.user.id)
        self.assertEqual(user_dict["created_at"], self.user.created_at.isoformat())
        self.assertEqual(user_dict["updated_at"], self.user.updated_at.isoformat())
        


    def test_attributes(self):
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")
        
    if __name__ == '__main__':
        unittest.main()
