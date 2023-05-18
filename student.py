import datetime
import book


class Student:
    def __init__(self, name, ID, email, book_limit=5):
        self.name = name
        self.ID = ID
        self.email = email
        self.books_taken = []
        self.book_limit = book_limit
        self.all_taken = []

    def __repr__(self):
        return f"Name-{self.name}, ID-{self.ID}"

    def borrow_book(self, book_):
        if not book_.get_available_copies():
            print("This book is currently not available.")
            return

        for i in self.books_taken:
            if i in book.Book.get_available_copies(book_):
                return f"You have this book copy"

        copy = book.Book.get_available_copies(book_)[0]
        if len(self.books_taken) >= self.book_limit:
            print("You have reached your borrowing limit.")
            return

        if copy.borrower == self:
            print("You have already borrowed this book.")
            return

        if copy.book in [book_copy.book for book_copy in self.books_taken]:
            print("You have already borrowed a copy of this book.")
            return

        due_date = datetime.date.today() + datetime.timedelta(days=14)
        copy.borrow(self, due_date)
        self.books_taken.append(copy)
        self.all_taken.append(copy)

    def return_book(self, book_):
        for i in self.books_taken:
            if i in book_.all_copy:
                i.return_copy()
                self.books_taken.remove(i)
                break
        else:
            print("You have not borrowed this book.")
            return

    def get_status(self):
        if not self.books_taken:
            print("You have not borrowed any books.")
            return

        print("Your borrowed books:")
        for copy in self.books_taken:
            due_date = copy.due_date
            if due_date is not None:
                print(f"{copy.book.title} (due date: {due_date})")
            else:
                print(f"{copy.book.title} (no due date)")

    @property
    def set_borrowing_limit(self, other=None):
        if other is None:
            return self.book_limit
        else:
            self.book_limit = other


student_1 = Student("John Doe", "123", "johndoe@example.com")
student_2 = Student("John Doe", "123", "johndoe@example.com")
student_3 = Student("John Doe", "123", "johndoe@example.com")



