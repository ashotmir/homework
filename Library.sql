CREATE DATABASE Library;

CREATE TABLE Author
(
    ID smallserial primary key,
    first_name varchar(50) not null,
    second_name varchar(50) not null
);

CREATE TABLE Book
(
    ID smallserial primary key,
    title varchar(100) not null,
    year_first_published int
);

CREATE TABLE BookAuthor
(
    author_id int REFERENCES Author(id) not null,
    book_id int REFERENCES Book(id) not null
);

CREATE TABLE BookCopies
(
    ID smallserial primary key,
    book_id int REFERENCES Book(id) not null,
    ISBN int,
    year_published int not null
);

CREATE TABLE Student
(
    ID smallserial primary key,
    first_name varchar(50) not null,
    second_name varchar(50) not null
);

CREATE TABLE Borrows
(
    ID smallserial primary key,
    book_copy_id int REFERENCES BookCopies(id) not null,
    student_id int REFERENCES Student(id) not null,
    borrow_date int not null,
    return_date int
);
