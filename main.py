from library_manager import LibraryManager
from utils import read_positive_int, read_nonempty

def main():
    library = LibraryManager()

    while True:
        print("\n=== Library Book Manager ===")
        print("1. Add book")
        print("2. View books")
        print("3. Search book")
        print("4. Borrow book")
        print("5. Return book")
        print("6. Library report")
        print("7. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            title = read_nonempty("Book title: ")
            author = read_nonempty("Author: ")
            library.add_book(title, author)
            print("Book added successfully.")

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            title = read_nonempty("Enter title to search: ")
            book = library.search_book(title)
            if book:
                print(f"{book['title']} | {book['author']} | {book['status']}")
            else:
                print("Book not found.")

        elif choice == "4":
            book_id = read_positive_int("Enter book ID: ")
            print(library.borrow_book(book_id))

        elif choice == "5":
            book_id = read_positive_int("Enter book ID: ")
            print(library.return_book(book_id))

        elif choice == "6":
            library.show_report()

        elif choice == "7":
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
