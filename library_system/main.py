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
                        isbn, title, author, year = parts [0], parts[1], parts[2], parts [3]
                        book = Book(isbn, title, author, int(year))
                        if len(parts) == 5 and parts[4] == "true":
                            book.borrow()
                        self.library.add_book(book)
            print(f"loaded {len(self.library.books)} books ")
        except FileNotFoundError:
            print("no book found")
    
    def save_books(self):
        with open("books.txt", "w") as f:
            for book in self.library.books:
                f.write(book.to_line() + "\n")
            print(f"saved {len(self.library.books)} books")
    
    def add_book(self):

        isbn = input("isbn: ")
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
        
        if book.borrow():
            self.save_books()
            print(f" borrowed: {book.title}")
        else:
            print("sorry book is already borrowed")
        
    def return_books(self):
        isbn = input("enter the book isbn: ")
        book = self.library.find_book(isbn)

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
            
    def report(self):

        report = "library report\n"
        report += f"generated: {__import__('datetime').datetime.now()}\n\n"

        report += "borrowed books: \n"
        borrowed = self.library.get_borrow_books()
        if borrowed:
            for book in borrowed:
                report += f" - {book.title} by {book.author}\n"
        else:
            report += "  none\n"
        
        report += "\navailable books: \n"
        avaialble = self.library.get_available_books()
        if avaialble:
            for book in avaialble:
                report += f" - {book.title} by {book.author} \n"
        else:
            report += " none\n"
        
        report += f"\n total books: {len(self.library.books)}\n"

        with open("report.txt", "w") as f:
            f.write(report)

        print(" report saved to report.txt")

    def menu(self):
        print("library management system")
        print("1. view all books")
        print("2. add new book")
        print("3. borrow book")
        print("4. return book")
        print("5. search books")
        print("6. make a report")
        print("7. exit")

    def run(self):
        print ("\nwelcome to the library system")

        while True:
            self.menu()
            choice = input("\nchoice (1-7)")

            if choice == '1':
                print(self.library.display_all())
            elif choice == '2':
                self.add_book()
            elif choice == '3':
                self.borrow_book()
            elif choice == '4':
                self.return_books()
            elif choice == '5':
                self.search_books()
            elif choice == '6':
                self.report()
            elif choice == '7':
                print("\nsaving and exiting")
                self.save_books()
                print("goodbye!")
                break
            else:
                print("invalid input")

if __name__ == "__main__":
    app = Libraryapp()
    app.run()