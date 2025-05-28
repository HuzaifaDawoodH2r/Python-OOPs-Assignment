#Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    totalBook = 0

    def __init__(self, book):
        self.book = book
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
       cls.totalBook += 1

book1 = Book("English")
book1 = Book("Math")
book1 = Book("Urdu")

print("Total Books Is = ",Book.totalBook)