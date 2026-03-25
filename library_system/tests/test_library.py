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
        self.assertFalse(validate_isbn("123456789"))
        self.assertFalse(validate_isbn("12-34-56-78"))
        self.assertFalse(validate_isbn("qwe-rty-uio"))

    def test_valid_year(self):
        self.assertTrue(validate_year(2024))
        self.assertTrue(validate_year(2000))
        self.assertTrue(validate_year(1900))
    
    def test_invalid_year(self):
        self.assertFalse(validate_year(1899))
        self.assertFalse(validate_year(2027))
        self.assertFalse(validate_year(99))