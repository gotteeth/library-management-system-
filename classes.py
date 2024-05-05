class Book:
    def __init__(self, title, author, isbn, genre, publication_date, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.publication_date = publication_date
        self.available = available

    def __str__(self):
        return f"{self.title} by {self.author} ({'Available' if self.available else 'Borrowed'})"

class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{book.title} has been borrowed.")
        else:
            print(f"{book.title} is currently unavailable.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{book.title} has been returned.")
        else:
            print("This book was not borrowed by this user.")

class Author:
    def __init__(self, name, biography=""):
        self.name = name
        self.biography = biography

    def __str__(self):
        return f"{self.name}: {self.biography}"
