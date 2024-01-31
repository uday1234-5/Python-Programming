class library:
    def __init__(self,book_list):
        self.book_list = book_list
        self.lended = {}
    
    def display_book(self):
        print("-"*60)
        print(f"{'Sr.no.':<10}{'Book Name':<15}")
        print("-"*60)
        for book in range(len(self.book_list)):
            print(f"{book+1:<10}{self.book_list[book]}")
        print("-"*60)
    def lend_book(self,book_name,user):
        if book_name not in self.lended.keys():
            self.lended.update({book_name:user})
            print(f"\"{book_name}\" book lended to user name Mr.\Mrs. {user}")
        else:
            print(f"**SORRY** \"{book_name}\" book already has been used by Mr.\Mrs. {self.lended[book_name]}.\n You can lend another book.")
            
    def add_book(self,addbook):
        self.book_list.append(addbook)
        print(f"\"{addbook}\" book added successfully")
            
    def returnbook(self,return_book):
        self.book_list.remove(return_book)
        print(f"\"{return_book}\" Book return successfully! ")
    
lib = library(['Python','JAVA','Maths','Physics','English'])

while 1:
   
    print("******************************************************************")
    print("   | Welcome to our KNOWLEDGE BASE LIBRARY MANAGEMENT SYSTEM |    ")
    print("******************************************************************")
    print("""1) Display Book
2) Lend Book
3) Add Book
4) Return Book""" )
    print("*******************************************************************")
                                                                        
    choice = eval(input("Enter Choice [1-4] to do some action with our KNOWLEDGEBASE Library : "))
    if choice == 1:
        lib.display_book()
    elif choice == 2:
        book_name = input("Enter book Name that you want to lend : ")
        user_name = input("Enter user Name : ")
        lib.lend_book(book_name,user_name)
    elif choice == 3:
        add_book = input("Enter book Name that you want to add : ")
        lib.add_book(add_book)
    elif choice == 4:
        return_book = input("Enter book Name that you want to return : ")
        lib.returnbook(return_book)
    else:
        print("Invalid choice!!! Please enter choice [1-4] : ")
        print("-"*60)
    
    print("Enter c to continue and q to exit")
    ch = ""
    while(ch != 'q' and ch != 'c'):
        
        ch = input()
        if ch == 'q':
            exit()
        elif ch == 'c':
            continue
        