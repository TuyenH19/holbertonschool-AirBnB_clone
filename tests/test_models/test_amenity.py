import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def setUp(self):
        """Set up a Place instance for testing."""
        self.amenity = Amenity()
        
    def test_attributes(self):
        self.assertEqual(self.amenity.name, "")
