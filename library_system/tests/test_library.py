import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.book import Book
from models.library import Library
from utilities.functions import validate_isbn, validate_year

class TestRegex(unittest.TestCase):
    