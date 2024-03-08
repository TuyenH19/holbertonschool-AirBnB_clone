import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        """Set up a Place instance for testing."""
        self.review = Review()
        
    def test_attributes(self):
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")
