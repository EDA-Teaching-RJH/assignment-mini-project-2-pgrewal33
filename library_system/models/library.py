class library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        for existing in self.books:
            if existing.isbn == book.isbn:
                return False
        self.books.append(book)
        return True
    
    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

