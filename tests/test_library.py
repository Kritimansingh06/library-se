import unittest
from src.library import Library

class TestLibrarySprint1(unittest.TestCase):

    def setUp(self):
        self.lib = Library()

    def test_add_book_success(self):
        self.lib.add_book(1, "Python", "Guido")
        self.assertIn(1, self.lib.books)

    def test_duplicate_book_id(self):
        self.lib.add_book(1, "Python", "Guido")
        with self.assertRaises(ValueError):
            self.lib.add_book(1, "Java", "James")

if __name__ == "__main__":
    unittest.main()

    def test_borrow_book(self):
        self.lib.add_book(1, "Python", "Guido")
        self.lib.borrow_book(1)
        self.assertEqual(self.lib.books[1]["status"], "Borrowed")

    def test_borrow_unavailable_book(self):
        self.lib.add_book(1, "Python", "Guido")
        self.lib.borrow_book(1)
        with self.assertRaises(ValueError):
            self.lib.borrow_book(1)

    def test_return_book(self):
        self.lib.add_book(1, "Python", "Guido")
        self.lib.borrow_book(1)
        self.lib.return_book(1)
        self.assertEqual(self.lib.books[1]["status"], "Available")
