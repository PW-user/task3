import unittest
from project import db, app
from project.books.models import Book

class TestBookModel(unittest.TestCase):
    def test_create_book(self):
        book = Book(
            name='Sample Book',
            author='John Doe',
            year_published=2022,
            book_type='Fiction',
            status='available'
        )

    def test_default_status_available(self):
        book = Book(
            name='Another Book',
            author='Jane Doe',
            year_published=2021,
            book_type='Non-Fiction'
        )

    def test_repr_method(self):
        book = Book(
            name='Test Book',
            author='Test Author',
            year_published=2020,
            book_type='Sci-Fi',
            status='borrowed'
        )

if __name__ == '__main__':
    unittest.main()
