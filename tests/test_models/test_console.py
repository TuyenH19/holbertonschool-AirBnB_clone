#!/usr/bin/python3
import unittest
import sys
from io import StringIO
from console import HBNBCommand



class Test_console(unittest.TestCase):
    """Unittests for testing console module."""

    def setUp(self):
        """Set up for the tests."""
        self.console = HBNBCommand()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        
    def tearDown(self):
        """Tear down for the tests."""
        sys.stdout = sys.__stdout__
        
    def test_quit(self):
        ''' Test quit exists'''
        console = self.create()
        self.assertTrue(console.onecmd("quit"))

    def test_EOF(self):
        ''' Test EOF exists'''
        console = self.create()
        self.assertTrue(console.onecmd("EOF"))

    def test_all(self):
        ''' Test all exists'''
        console = self.create()
        console.onecmd("all")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

if __name__ == '__main__':
    unittest.main()