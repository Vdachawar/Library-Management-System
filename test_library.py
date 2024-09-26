import unittest
from library import Book, Library  # Ensure this import matches your library file name

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("1234", "Book One", "Author A", 2020)
        self.book2 = Book("5678", "Book Two", "Author B", 2021)
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

    def test_add_book(self):
        self.assertIn(self.book1, self.library.books)

    def test_borrow_book(self):
        self.library.borrow_book("1234")
        self.assertFalse(self.book1.is_available)

    def test_return_book(self):
        self.library.borrow_book("1234")
        self.library.return_book("1234")
        self.assertTrue(self.book1.is_available)

    def test_view_available_books(self):
        self.assertIn("Book One", self.library.view_available_books())

if __name__ == '__main__':
    unittest.main()
