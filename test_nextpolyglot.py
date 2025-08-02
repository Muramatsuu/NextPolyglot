# test_nextpolyglot.py
"""
Tests for NextPolyglot module.
"""

import unittest
from nextpolyglot import NextPolyglot

class TestNextPolyglot(unittest.TestCase):
    """Test cases for NextPolyglot class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NextPolyglot()
        self.assertIsInstance(instance, NextPolyglot)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NextPolyglot()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
