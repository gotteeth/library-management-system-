from classes import Book, User, Author

def main_menu():
    while True:
        print("\nwelcome to the library management system")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")
        choice = input("Select an option: ")
        if choice == "1":
            book_operations()
        elif choice == "2":
            user_operations()
        elif choice == "3":
            author_operations()
        elif choice == "4":
            print("Exiting system.")
            break
        else:
            print("Invalid choice, please try again.")

def book_operations():
    print("\n--- Book Operations ---")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")
   

def user_operations():
    print("\n--- User Operations ---")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")
    

def author_operations():
    print("\n--- Author Operations ---")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")
   

if __name__ == "__main__":
    main_menu()
