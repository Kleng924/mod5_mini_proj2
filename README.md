CREATE DATABASE LibraryDB;
USE LibraryDB;

-- Books Table
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT,
    isbn VARCHAR(13) NOT NULL UNIQUE,
    publication_date DATE,
    availability BOOLEAN DEFAULT 1,
    FOREIGN KEY (author_id) REFERENCES authors(id) ON DELETE CASCADE
);

-- Authors Table
CREATE TABLE authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    biography TEXT
);

-- Users Table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    library_id VARCHAR(10) NOT NULL UNIQUE
);

-- Borrowed Books Table
CREATE TABLE borrowed_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    book_id INT,
    borrow_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE
);

import mysql.connector

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",  # Change if you have a different MySQL user
            password="yourpassword",  # Change this to your MySQL password
            database="LibraryDB"
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

from db import get_connection

class Book:
    def __init__(self, title, author_id, isbn, publication_date):
        self.title = title
        self.author_id = author_id
        self.isbn = isbn
        self.publication_date = publication_date
        self.availability = True

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author_id, isbn, publication_date, availability) VALUES (%s, %s, %s, %s, %s)", 
                       (self.title, self.author_id, self.isbn, self.publication_date, self.availability))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        conn.close()
        return books

from db import get_connection

class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, library_id) VALUES (%s, %s)", (self.name, self.library_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        conn.close()
        return users

from db import get_connection

class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (name, biography) VALUES (%s, %s)", (self.name, self.biography))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors")
        authors = cursor.fetchall()
        conn.close()
        return authors

from classes.book import Book
from classes.user import User
from classes.author import Author

def main_menu():
    while True:
        print("\nWelcome to the Library Management System with Database Integration!")
        print("1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit")
        choice = input("Select an option: ")

        if choice == '1':
            book_menu()
        elif choice == '2':
            user_menu()
        elif choice == '3':
            author_menu()
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice.")

def book_menu():
    while True:
        print("\nBook Operations:")
        print("1. Add a new book\n2. Display all books\n3. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author_id = input("Enter author ID: ")
            isbn = input("Enter ISBN: ")
            pub_date = input("Enter publication date (YYYY-MM-DD): ")
            book = Book(title, author_id, isbn, pub_date)
            book.save()
            print("Book added successfully!")

        elif choice == '2':
            books = Book.get_all()
            for book in books:
                print(book)

        elif choice == '3':
            break
        else:
            print("Invalid choice.")

def user_menu():
    while True:
        print("\nUser Operations:")
        print("1. Add a new user\n2. Display all users\n3. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter user name: ")
            library_id = input("Enter Library ID: ")
            user = User(name, library_id)
            user.save()
            print("User added successfully!")

        elif choice == '2':
            users = User.get_all()
            for user in users:
                print(user)

        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()

