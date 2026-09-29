# Library Book Manager

A simple command-line Python project for managing books in a small library.

## Features

- Add books
- View all books
- Search books by title
- Borrow a book
- Return a book
- Show a library report
- Input validation

## Python Concepts Used

- Variables and data types
- `if`, `elif`, and `else`
- `for` and `while` loops
- Lists and dictionaries
- Functions
- Classes and objects
- Modules and imports
- Exception handling
- Searching and counting algorithms

## Requirements

- Python 3.9 or later
- No external packages

## Run the Project

Open a terminal in this folder and run:

```bash
python main.py
```

## Run Tests

```bash
python -m unittest discover -s tests -v
```

## Folder Structure

```text
library-book-manager/
├── main.py
├── book.py
├── library_manager.py
├── reports.py
├── utils.py
├── statement.md
├── README.md
└── tests/
    └── test_library.py
```

## Example

```text
=== Library Book Manager ===
1. Add book
2. View books
3. Search book
4. Borrow book
5. Return book
6. Library report
7. Exit
Enter choice: 1
Book title: Python Basics
Author: John Smith
Book added successfully.
```

## Notes

The application is intentionally simple and uses only Python's standard library so that the code is easy to understand and explain.
