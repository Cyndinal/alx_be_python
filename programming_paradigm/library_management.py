

"""
Implement a Book class with public attributes
title and author, and a private attribute _is_checked_out
to track its availability.

=============================================================
Implement a Library class with a private list _books to
store instances of Book. Include methods to
add_book,
check_out_book(title),
return_book(title),
list_available_books.
================================================================
"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return f'You have checked out "{title}".'
        return f'Sorry, "{title}" is not available.'

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return f'You have returned "{title}".'
        return f'Sorry, "{title}" was not checked out.'

    def list_available_books(self):
        available_books = [book.title for book in self._books if book.is_available()]
        return available_books if available_books else "No books available."

# Example usage:
# library = Library()
# book1 = Book("1984", "George Orwell")
# book2 = Book("To Kill a Mockingbird", "Harper Lee")
#
# library.add_book(book1)
# library.add_book(book2)

# print(library.list_available_books())  # ['1984', 'To Kill a Mockingbird']
# print(library.check_out_book("1984"))  # You have checked out "1984".
# print(library.list_available_books())  # ['To Kill a Mockingbird']
# print(library.return_book("1984"))     # You have returned "1984".
# print(library.list_available_books())  # ['1984', 'To Kill a Mockingbird']
