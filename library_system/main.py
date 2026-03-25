from models.book import book
from models.library import library
from utilities.functions import validate_isbn, validate_year, clean_text

class libraryapp:
    def __init__(self):
        self.library =  library()
        self.load_books()

    def load_books(self):

        try:
            with open("books.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) >= 4:
                        isbn, title, author, year = parts [0], parts[1], parts[2], parts [3], parts[4]
                        book = book(isbn, titile, author, int(year))
                        if len(parts) == 5 and parts[4] == "true":
                            book.borrow()
                        self.library.add_book(book)
            print(f"loaded {len(self.library.books)} books ")
        except FileNotFoundError:
            print("no book found")