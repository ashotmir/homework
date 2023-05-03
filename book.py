import datetime


class Book:
    books = []

    def __init__(self, title, authors, year, ISBN, genre, copy=1, rating=5):
        self.title = title
        self.authors = authors
        self.year = year
        self.ISBN = ISBN
        self.genre = genre
        self.rating = rating
        self.books.append(self.ISBN)
        self.all_copy = []
        for i in range(copy):
            self.all_copy.append(BookCopy(self, i + 1))
        self.books.append(self)

    def add_copy(self, other):
        for i in range(self.all_copy[-1].copy_id, self.all_copy[-1].copy_id + other):
            self.all_copy.append(BookCopy(self, len(self.all_copy) + 1))

    def get_available_copies(self):
        available_copies = [copy for copy in self.all_copy if copy.availability_status]
        return available_copies

    def __repr__(self) -> str:
        return f"Title-{self.title} -- Authors-{self.authors}"


class BookCopy:
    def __init__(self, book, copy_id, condition_rating=5):
        self.book = book
        self.copy_id = copy_id
        self.borrower = None
        self.due_date = None
        self.availability_status = True
        self.condition_rating = condition_rating

    def borrow(self, borrower, date):
        self.borrower = borrower
        self.due_date = date
        self.availability_status = False

    def return_copy(self):
        self.borrower = None
        self.due_date = None
        self.availability_status = True

    def change_condition_rating(self, new_rating):
        self.condition_rating = new_rating

    def __repr__(self):
        return f"BookCopy({self.book}, {self.copy_id})"


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "1234567890", "Fiction", copy=5)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "0987654321", "Fiction")
book3 = Book("1984", "George Orwell", 1949, "1357908642", "Science Fiction")

