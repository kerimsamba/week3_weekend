import unittest

from models.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.test_book = Book("A book", "An author", "A genre")

    def test_book_has_name(self):
        self.assertEqual("A book", self.test_book.title)

    def test_book_has_author(self):
        self.assertEqual("An author", self.test_book.author)

    def test_book_has_genre(self):
        self.assertEqual("A genre", self.test_book.genre)

    
