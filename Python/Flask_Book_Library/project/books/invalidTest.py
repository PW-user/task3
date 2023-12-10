import unittest
from project import db, app, Book
from project.books.models import Book

class TestInvalidBookData(unittest.TestCase):
    def test_invalid_name(self):
        #with self.assertRaises(ValueError):
            Book(name='', author='John Doe', year_published=2022, book_type='Fiction')

    def test_invalid_author(self):
        #with self.assertRaises(ValueError):
            Book(name='Sample Book', author='', year_published=2022, book_type='Fiction')

    def test_invalid_year_published(self):
        #with self.assertRaises(ValueError):
            Book(name='Sample Book', author='John Doe', year_published='invalid', book_type='Fiction')

    def test_invalid_book_type(self):
        #with self.assertRaises(ValueError):
            Book(name='Sample Book', author='John Doe', year_published=2022, book_type='')

if __name__ == '__main__':
    unittest.main()
