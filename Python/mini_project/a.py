empty = {}

while True:
    print("1. Add books : ")
    print("2. Remove Books : ")
    print("3. Search Books : ")
    print("4. Display all book : ")
    print("5. Exist")
    print("\n")
    choice = input("Enter your choice(1-5) : ")
        
    if choice == "1":
        Book_id = input("Enter the Book ID : ")
        Book_name = input("Enter Book Name : ")
        Book_author = input("Enter authon name : ")
        empty[Book_id] = {"Name ":Book_name,"Author ":Book_author}
        print(empty)
        print("Book added successfully . ")
        print("\n")
    
    elif choice == "2":
        y = input("Enter the Book ID : ")
        if y in empty:
            del empty[y]
            print(empty)
            print("Book removed successfully .")
        else:
            print(f"Book are not found in library.")
    elif choice == "3":
        Book_id = input("Enter book id it search book : ")
        if Book_id in empty:
            Book_details = empty[Book_id]
            print(f"Name : {Book_details['Name ']}")
            print(f"Author : {Book_details['Author ']}")
        else:
            print(f"Book are not found in library.")
    elif choice == "4":
        if empty:
            print("ID \t\t Book \t\t Author name")
            print("-"*60)
            for x,y in empty.items():
                print(f"{x}\t\t{y['Name ']}\t\t\t{y['Author ']}")
        else:
            print("Library is empty!")
    elif choice == "5":
        print("Existing the library management system.....")   
        break
    else:
        print("Invalid Choice ! Please enter the number between 1 and 5")
        
        
        
            
        
        
        
        
    