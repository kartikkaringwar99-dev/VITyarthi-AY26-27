from book import Book

class LibraryManager:
    def __init__(self):
        self.books = []
        self.next_id = 1

    def add_book(self, title, author):
        book = Book(self.next_id, title, author)
        self.books.append(book.to_dict())
        self.next_id += 1

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return

        for book in self.books:
            print(f"{book['id']}. {book['title']} | {book['author']} | {book['status']}")

    def search_book(self, title):
        for book in self.books:
            if title.lower() in book["title"].lower():
                return book
        return None

    def borrow_book(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                if book["status"] == "Borrowed":
                    return "Book is already borrowed."
                book["status"] = "Borrowed"
                return "Book borrowed successfully."
        return "Book ID not found."

    def return_book(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                if book["status"] == "Available":
                    return "Book is already available."
                book["status"] = "Available"
                return "Book returned successfully."
        return "Book ID not found."

    def show_report(self):
        total = len(self.books)
        borrowed = sum(book["status"] == "Borrowed" for book in self.books)
        available = total - borrowed

        print("\n--- Library Report ---")
        print(f"Total books : {total}")
        print(f"Available   : {available}")
        print(f"Borrowed    : {borrowed}")
