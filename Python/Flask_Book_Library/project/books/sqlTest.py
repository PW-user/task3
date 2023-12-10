import unittest
from project import db, app, Book
from project.books.models import Book

class TestSQLInjectionAttacks(unittest.TestCase):
    def test_sqli_in_name(self):
        with self.assertRaises(ValueError):
            Book(name="-- or #", author='John Doe', year_published=2022, book_type='Fiction')

    def test_sqli_in_author(self):
        with self.assertRaises(ValueError):
            Book(name='Sample Book', author="\" OR 1 == 1 -- -", year_published=2022, book_type='Fiction')

    def test_sqli_in_year_published(self):
        with self.assertRaises(ValueError):
            Book(name='Sample Book', author='John Doe', year_published="\'\'\'\'\'\'\'\'\'\'\'\''UNION SELECT '2", book_type='Fiction')

    def test_sqli_in_book_type(self):
        with self.assertRaises(ValueError):
            Book(name='Sample Book', author='John Doe', year_published=2022, book_type="1' ORDER BY 1--+", status='Fiction')

    def test_sqli_in_status(self):
        with self.assertRaises(ValueError):
            Book(name='Sample Book', author='John Doe', year_published=2022, book_type='Fiction', status="' or '1'='1'--")

    def test_sqli_in_multiple_fields(self):
        with self.assertRaises(ValueError):
            Book(name="-- or \#\", author="\" OR 1 == 1 -- -", year_published="'''''''''''''UNION SELECT '2", book_type="1' ORDER BY 1--+", status="' or '1'='1'--")

if __name__ == '__main__':
    unittest.main()
