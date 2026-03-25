from models.book import Book
from models.library import Library
from utilities.functions import validate_isbn, validate_year, clean_text

class Libraryapp:
    def __init__(self):
        self.library =  Library()
        self.load_books()

    def load_books(self):

        try:
            with open("books.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) >= 4:
                        isbn, title, author, year = parts [0], parts[1], parts[2], parts [3], parts[4]
                        book = book(isbn, title, author, int(year))
                        if len(parts) == 5 and parts[4] == "true":
                            book.borrow()
                        self.library.add_book(book)
            print(f"loaded {len(self.library.books)} books ")
        except FileNotFoundError:
            print("no book found")
    
    def save_books(self):
        with open("books.txt", "w") as f:
            for book in self.library.books:
                f.write(book.to_line()) + "\n"
            print(f"saved {len(self.library.books)} books")
    
    def add_book(self):

        isbn = input(isbn: )
        if not validate_isbn(isbn):
            print ("invalid isbn!")
            return
        if self.library.find_book(isbn):
            print ("book already exists")
            return
        
        title = input("title: ")
        author = input("author: ")

        try:
            year = int(input("year: "))
            if not validate_year(year):
                print("invalid year! ")
                return
        
        except ValueError:
            print("invalid year")
            return
        
        book = Book(isbn, title, author, year)
        self.library.add_book(book)
        self.save_books()
        print(f"added: {title}")

    def borrow_book(self):
        isbn = input("enter isbn of the book you want to borrow: ")
        book = self.library.find_book(isbn)

        if not book:
            print("book not found")
            return
        
        if book.borrowed():
            self.save_books()
            print(f" borrowed: {book.title}")
        else:
            print("sorry book is already borrowed")
        
    def return_books(self):
        isbn = input("enter the book isbn: ")
        book = self.library.fiid_book(isbn)

        if not book:
            print("book not found")
            return
        if book.return_book():
            self.save_books()
            print(f"returned: {book.title}")
        else:
            print("this book is not borrowed")
        
    def search_books(self):

        term = input("enter search term:")
        results = self.library.search(term)

        if results:
            print(f"\n found {len(results)} books:")
            for book in results:
                print(f" {book.display()}")
        else:
            print("no books found")
            
