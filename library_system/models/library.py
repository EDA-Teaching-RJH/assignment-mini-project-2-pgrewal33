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

    def search(self,term):
        term_lower = term.lower()
        results = []
        for book in self.books:
            if term_lower in book.title.lower() or term_lower in book.author.lower():
                results.append(book)
        return results

    def get_borrow_books(self):
        return [book for book in self.books if book.is_borrowed]
    
    def get_available_books(self):
        return [book for book in self.books if not book.is_borrowed]
    
    def display_all(self):
        if not self.books:
            return "no books in libary"
        
        result = "\n" + "="*10 + "\n"
        result += "library catalog\n"
        result += "="*10 + "\n"

        for book in self.books:
            result += book.display() + "\n"

        result += "="*10 + "\n"
        result += f"total books: {len(self.books)}\n"
        result += f"available: {len(self.get_available_books())}\n"
        result += f"borrowed: {len(self.get_borrow_books())}\n"

        return result
    
