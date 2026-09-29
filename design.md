# Design Notes

## Functional Requirements

1. Add a book with title and author.
2. Display all books.
3. Search for a book.
4. Borrow and return books.
5. Generate a simple library report.

## Non-Functional Requirements

- Usability: menu-based terminal interface.
- Reliability: invalid input is handled.
- Maintainability: related functions are separated into modules.
- Portability: no third-party packages are required.

## Workflow

Start -> Menu -> Select operation -> Process book record -> Display result -> Return to menu -> Exit

## Class Relationship

`LibraryManager` manages book records created from the `Book` class.

## Storage

Records are stored in memory while the program is running.
