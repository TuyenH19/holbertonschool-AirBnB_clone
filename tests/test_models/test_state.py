import unittest
from models.state import State


class TestReview(unittest.TestCase):
    def setUp(self):
        """Set up a Place instance for testing."""
        self.state = State()
        
    def test_attributes(self):
        self.assertEqual(self.state.state_id, "")
        self.assertEqual(self.state.name, "")
