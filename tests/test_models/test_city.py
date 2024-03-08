import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()
    
    def test_attributes(self):
        """Test the attributes of city"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")
        
        if __name__ == '__main__':
            unittest.main()