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

class TestBook(unittest.TestCase):
    def test_create_books(self):
        book = Book("123-456-789", "TEST BOOK", "TEST AUTHOR", 2024)
        self.assertEqual(book.title, "TEST BOOK")
        self.assertEqual(book.author, "TEST AUTHOR")
        self.assertFalse(book.is_borrowed)

    def test_borrow_book(self):
        book = Book("123-456-789", "TEST", "AUTHOR", 2024)
        result = book.borrow()
        self.assertTrue(result)
        self.assertTrue(book.is_borrowed)

    def test_borrow_book(self):
        book = Book("123-456-789", "TEST", "AUTHOR", 2024)
        book.borrow()
        result = book.borrow()
        self.assertFalse(result)
    
    def test_return_book(self):
        book = Book("123-456-789", "TEST", "AUTHOR", 2024)
        book.borrow()
        result = book.return_book()
        self.assertTrue(result)
        self.assertFalse(book.is_borrowed)
    
    def test_returned_unborrowed_book(self):
        book = Book("123-456-789", "TEST", "AUTHOR", 2024)
        result = book.return_book()
        self.assertFalse(result)

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("111-111-111", "python programming", "john smith", 2024)
        self.book2 = Book("222-222-222", "java basics", "jane doe", 2023)
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

    def test_add_book(self):
        new_book = Book("333-333-333", "new book", "new author", 2024)
        result = self.library.add_book(new_book)
        self.assertTrue(result)
        self.assertEqual(len(self.library.books), 3)
    
    def test_add_duplicate_book(self):
        duplicate = Book("111-111-111", "duplicate", " bob smith", 2024)
        result = self.library.add_book(duplicate)
        self.assertFalse(result)
        self.assertEqual(len(self.library.books), 2)
    
    def test_find_book(self):
        book = self.library.find_book("111-111-111")
        self.assertIsNotNone(book)
        self.assertEqual(book.title, "python programming")
    
    def test_find_book_not_exists(self):
        book = self.library.find_book("999-999-999")
        self.assertIsNone(book)

    def search_by_title(self):
        results = self.library.search("python")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "python programming")

    def test_search_by_author(self):
        results = self.library.search("smith")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].author, "john smith")
    
    def test_search_no_results(self):
        results = self.library.search("notmatch")
        self.assertEqual(len(results), 0)

    def test_borrowed_books(self):
        self.book1.borrow()
        borrowed = self.library.get_borrow_books()
        self.assertEqual(len(borrowed), 1)
        self.assertEqual(borrowed[0].title, "python programming")

    def test_available_books(self):
        print(f"\nBefore borrow - book1.is_borrowed: {self.book1.is_borrowed}")
        self.book1.borrow
        print(f"After borrow - book1.is_borrowed: {self.book1.is_borrowed}")
        available = self.library.get_available_books()
        print(f"Number of available books: {len(available)}")
        self.assertEqual(len(available), 1)
        self.assertEqual(available[0].title, "java basics")

if __name__ == "__main__":
    unittest.main()