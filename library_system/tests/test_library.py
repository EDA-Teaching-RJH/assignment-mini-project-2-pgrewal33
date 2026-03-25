import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.book import Book
from models.library import Library
from utilities.functions import validate_isbn, validate_year

class TestRegex(unittest.TestCase):
    def test_valid_isbn(self):
        self.assertTrue(validate_isbn("123-456-789"))
        self.assertTrue(validate_isbn("987-123-456"))

    def test_invalid_isbn(self):
        self.assertTrue(validate_isbn("123456789"))
        self.assertTrue(validate_isbn("12-34-56-78"))
        self.assertTrue(validate_isbn("qwe-rty-uio"))
        