from classes.book import Book
from classes.user import User

def main_menu():
    while True:
        print("\nLibrary Management System with Database Integration")
        print("1. Book Operations\n2. User Operations\n3. Quit")
        choice = input("Select an option: ")

        if choice == '1':
            book_menu()
        elif choice == '2':
            user_menu()
        elif choice == '3':
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