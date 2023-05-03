import student as student_


class Library:
    def __init__(self):
        self.books = []
        self.students = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def change_borrowing_limit(self, student, new_limit):
        student.set_borrowing_limit(new_limit)

    def see_all_books(self):
        return self.books

    def see_available_books(self):
        available_books = []
        for book in self.books:
            for copy in book.all_copy:
                if copy.availability_status:
                    available_books.append(book)
                    break
        return available_books

    def search_books(self, title=None, author=None, year=None, isbn=None, genre=None):
        matches = []
        for book in self.books:
            if title and title.lower() not in book.title.lower():
                continue
            if author and author.lower() not in [a.lower() for a in book.authors]:
                continue
            if year and book.year != year:
                continue
            if isbn and book.isbn != isbn:
                continue
            if genre and genre.lower() not in book.genre.lower():
                continue
            matches.append(book)
        return matches


library = Library()
library.add_book(student_.book.book1)
library.add_book(student_.book.book2)
library.add_book(student_.book.book3)
library.add_student(student_.student_1)
library.add_student(student_.student_2)
library.add_student(student_.student_3)


