class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f'"{self.title}" has been borrowed.')
        else:
            print(f'"{self.title}" is already borrowed.')

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f'"{self.title}" has been returned.')
        else:
            print(f'"{self.title}" was not borrowed.')


class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Book "{book.title}" added to library.')

    def register_patron(self, patron):
        self.patrons.append(patron)
        print(f'Patron "{patron.name}" registered.')

    def borrow_book(self, patron_id, isbn):
        patron = None
        book = None

        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p
                break

        for b in self.books:
            if b.isbn == isbn:
                book = b
                break

        if patron and book:
            if not book.is_borrowed:
                book.borrow()
                patron.borrow_book(book)
            else:
                print("Book is not available.")
        else:
            print("Invalid Patron ID or ISBN.")

    def return_book(self, patron_id, isbn):
        patron = None
        book = None

        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p
                break

        for b in self.books:
            if b.isbn == isbn:
                book = b
                break

        if patron and book:
            if book in patron.borrowed_books:
                book.return_book()
                patron.return_book(book)
            else:
                print("This patron did not borrow the book.")
        else:
            print("Invalid Patron ID or ISBN.")


# Main Program
library = Library()

book1 = Book("Python Programming", "Guido van Rossum", "101")
book2 = Book("Data Structures", "Mark Allen", "102")
book3 = Book("Machine Learning", "Tom Mitchell", "103")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

patron1 = Patron("Alice", 1)
patron2 = Patron("Bob", 2)

library.register_patron(patron1)
library.register_patron(patron2)

library.borrow_book(1, "101")
library.borrow_book(2, "102")

library.return_book(1, "101")

print("\nLibrary Books Status:")
for book in library.books:
    status = "Borrowed" if book.is_borrowed else "Available"
    print(f"{book.title} - {status}")

print("\nPatrons Information:")
for patron in library.patrons:
    print(f"\nPatron: {patron.name}")
    if patron.borrowed_books:
        print("Borrowed Books:")
        for book in patron.borrowed_books:
            print(book.title)
    else:
        print("No books borrowed.")