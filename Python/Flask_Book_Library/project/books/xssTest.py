import unittest
from project import db, app, Book
from project.books.models import Book

class TestXSSAttacks(unittest.TestCase):
    def test_xss_in_name(self):
        with self.assertRaises(ValueError):
            Book(name="\"-prompt(8)-\"", author='John Doe', year_published=2022, book_type='Fiction')

    def test_xss_in_author(self):
        with self.assertRaises(ValueError):
            Book(name='Sample Book', author="'-prompt(8)-'", year_published=2022, book_type='Fiction')

    def test_xss_in_year_published(self):
        with self.assertRaises(ValueError):
            Book(name='Sample Book', author='John Doe', year_published='<img/src/onerror=prompt(8)-\>', book_type='Fiction')

    def test_xss_in_book_type(self):
        with self.assertRaises(ValueError):
            Book(name='Sample Book', author='John Doe', year_published=2022, book_type="<script>alert('XSS')</script>")

    def test_xss_in_status(self):
        with self.assertRaises(ValueError):
            Book(name='Sample Book', author='John Doe', year_published=2022, book_type='Fiction', status="'`\"><\\x3Cscript>javascript:alert(1)\"></script>")

if __name__ == '__main__':
    unittest.main()
