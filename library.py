# Initialize an empty library dictionary
library = {}

while True:
    print("==== Library Management System ====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Display All Books")
    print("5. Exit")
    print("\n")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        book_id = input("Enter book ID: ")
        book_name = input("Enter book name: ")
        author = input("Enter author name: ")

        # Add book details to the library dictionary
        library[book_id] = {"name": book_name, "author": author}

        print("Book added successfully!")

    elif choice == "2":
        book_id = input("Enter book ID to remove: ")

        if book_id in library:
            del library[book_id]
            print("Book removed successfully!")
        else:
            print("Book not found in the library!")

    elif choice == "3":
        book_id = input("Enter book ID to search: ")

        if book_id in library:
            book_details = library[book_id]
            print(f"Book Name: {book_details['name']}")
            print(f"Author: {book_details['author']}")
        else:
            print("Book not found in the library!")

    elif choice == "4":
        if library:
            print("Books in the library:")
            print("Book ID\t\tBook Name\t\tAuthor")
            print("-" * 50)
            for book_id, book_details in library.items():
                print(f"{book_id}\t\t{book_details['name']}\t\t\t{book_details['author']}")
        else:
            print("Library is empty!")

    elif choice == "5":
        print("Exiting the library management system...")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 5.")
