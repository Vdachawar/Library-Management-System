class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.is_available:
                book.is_available = False
                return f"You've borrowed '{book.title}'"
        raise Exception("Book not available")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.is_available = True
                return f"'{book.title}' returned successfully"
        raise Exception("Book not found")

    def view_available_books(self):
        return [book.title for book in self.books if book.is_available]
