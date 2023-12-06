library = {}

while True:
    print("1. Add Books")
    print("2. Remove Books")
    print("3. Search Books")
    print("4. Display all Books")
    print("5. Exist")
    
    choice = input("Enter your choice (1-5) => ")
    
    if choice == "1":
        book_id = input("Enter book id : ")
        book_name = input("Enter book name : ")
        author_name = input("Enter Author name : ")
        library[book_id] = {"Book Name":book_name,"Author Name":author_name}
        print(library)
        print("Book added succesfully.")
    elif choice == "2":
        book_id = input("Enter book id that you want to remove : ")
        if book_id in library:
            del library[book_id]
            print("Book is deleted.")
            print(library)        
        else:
            print("Book is not found in library.")
    elif choice == "3":
        book_id = input("Enter book id to search book => ")
        if book_id in library:
            book_details = library[book_id]
            print(f"'Book Name': {book_details['Book Name']}")
            print(f"'Author Name': {book_details['Author Name']}")
        else:
            print("No book found :")
    elif choice == "4":
        if library:
            print("ID \t\t Book name \t\t Author name")
            print("-"*70)
            for x,y in library.items():
                print(f"{x}\t\t{y['Book Name']}\t\t{y['Author Name']}")
        else:
            print("no book is found")
        
            
        