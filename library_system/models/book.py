class Book:

    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False
    
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False
    
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False
    
    def display(self):
        status = "borrowed" if self.is_borrowed else "available"
        return f"{self.isbn} - {self.title} - {self.author} - {self.year} - {status}"
    
    def to_line(self):
        return f"{self.isbn}, {self.title}, {self.author}, {self.year}, {self.is_borrowed}"