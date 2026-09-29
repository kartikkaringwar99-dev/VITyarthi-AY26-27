import unittest
from library_manager import LibraryManager
from reports import library_summary

class TestLibraryManager(unittest.TestCase):

    def setUp(self):
        self.library = LibraryManager()
        self.library.add_book("Python Basics", "John Smith")
        self.library.add_book("Data Structures", "Jane Doe")

    def test_search_book(self):
        book = self.library.search_book("python")
        self.assertIsNotNone(book)
        self.assertEqual(book["author"], "John Smith")

    def test_borrow_and_return(self):
        self.assertEqual(self.library.borrow_book(1), "Book borrowed successfully.")
        self.assertEqual(self.library.books[0]["status"], "Borrowed")
        self.assertEqual(self.library.return_book(1), "Book returned successfully.")
        self.assertEqual(self.library.books[0]["status"], "Available")

    def test_report(self):
        self.library.borrow_book(1)
        report = library_summary(self.library.books)
        self.assertEqual(report["total"], 2)
        self.assertEqual(report["borrowed"], 1)
        self.assertEqual(report["available"], 1)

if __name__ == "__main__":
    unittest.main()
