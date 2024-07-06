class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Copies: {self.copies}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.copies > 0:
            book.copies -= 1
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"Sorry, {book.title} is not available right now.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.copies += 1
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} doesn't have {book.title}.")

    def __str__(self):
        borrowed_books_titles = ", ".join([book.title for book in self.borrowed_books])
        return f"Name: {self.name}, Member ID: {self.member_id}, Borrowed Books: {borrowed_books_titles}"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book {book.title} added to the library.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member {member.name} added to the library.")

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def __str__(self):
        books_str = "\n".join([str(book) for book in self.books])
        members_str = "\n".join([str(member) for member in self.members])
        return f"Library Books:\n{books_str}\n\nLibrary Members:\n{members_str}"


# Example usage:

# Create books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "123456789", 3)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "987654321", 2)

# Create members
member1 = Member("Alice", "M001")
member2 = Member("Bob", "M002")

# Create library
library = Library()

# Add books and members to the library
library.add_book(book1)
library.add_book(book2)
library.add_member(member1)
library.add_member(member2)

# Members borrow books
member1.borrow_book(book1)
member2.borrow_book(book2)

# Print library status
print(library)

# Members return books
member1.return_book(book1)
member2.return_book(book2)

# Print library status
print(library)
