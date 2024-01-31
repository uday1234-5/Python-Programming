 #library management system

class library:
   def __init__(self, l_books,libraryname):
       self.booklist = l_books
       self.libraryname = libraryname
       self.lendict={}
       
   def displaybooks(self):
       print("we have following books in our library {}".format(self.libraryname))
       print("==============================================================")
       for book in self.booklist:
           print("\t\t",book)
           
   def lendbook(self,user,book):
       if book not in self.lendict.keys():
           self.lendict.update({book:user})
           print("***\tbook lended to user {}***".format(user))
       else:
           print("***\tbook already being used by {}***".format(self.lendict[book]))
           
   def addbook(self,book):
       self.booklist.append(book)
       print("***\tnew book named {} added to our library***".format(book))
       
   def returnbook(self,book):
       self.lendict.pop(book)
lib=library(["python","java","C basics","C++"],"knowledgebase")
while(True):
   print("welcome to our library {}. enter your choice to continue".format(lib.libraryname))
   print("==============================================================================")
   print("1.display books")
   print("2.lend a book")
   print("3.add a book")
   print("4.return a book")
   
   choice=int(input())
   if choice == 1:
       lib.displaybooks()
   elif choice == 2:
       book = input("enter the name of book you want to lend:")
       user = input("enter user name:")
       print("==========================================================================")
       lib.lendbook(user,book)
   elif choice == 3:
       book = input("enter the name of bookc you want to add:")
       print("==========================================================================")
       lib.addbook(book)
   elif choice == 4:
       book = input("enter the name of book you want to return: ")
       print("==========================================================================")
       lib.returnbook(book)
   else:
       print("not a valid choice")
   print("==============================================================================")

   print("enter q to exist and c to continue")
   ch=""
   while(ch != "c" and ch != "q"):
       ch = input()
       if(ch=="q"):
           exit()
       elif(ch=="c"):
           continue


 #library management system

# class library:
#    def __init__(self, l_books,libraryname):
#        self.booklist = l_books
#        self.libraryname = libraryname
#        self.lendict={}
       
#    def displaybooks(self):
#        print(f"we have following books in our library {self.libraryname}")
#        print("="*60)
#        print(f"{'Sr.no.':<15}{'Book Name':<15}")
#        for book in range(0,len(self.booklist)):
#            print(f"{book+1:<15}{self.booklist[book]:<15}")
           
#    def lendbook(self,user,book):
#        if book not in self.lendict.keys():
#            self.lendict.update({book:user})
#            print(f" Book lended to user Mr./Mrs.{user} ***")
#        else:
#            print(f"***\tBook already being used by Mr./Mrs.{self.lendict[book]}***")
           
#    def addbook(self,book):
#        self.booklist.append(book)
#        print(f"***\tNew book named {book} added to our library \t***")
       
#    def returnbook(self,book):
#        self.lendict.pop(book)
# lib = library(["python","java","C basics","C++"],"knowledgebase")
# while(True):
#    print("welcome to our library {}. enter your choice to continue".format(lib.libraryname))
#    print("="*60)
#    print("1.display books")
#    print("2.lend a book")
#    print("3.add a book")
#    print("4.return a book")
   
#    choice=int(input("Enter choice from 1-4 : "))
#    if choice == 1:
#        lib.displaybooks()
#    elif choice == 2:
#        book = input("enter the name of book you want to lend:")
#        user = input("enter user name:")
#        print("="*60)
#        lib.lendbook(user,book)
#    elif choice == 3:
#        book = input("enter the name of bookc you want to add:")
#        print("="*60)
#        lib.addbook(book)
#    elif choice == 4:
#        book = input("enter the name of book you want to return: ")
#        print("="*60)
#        lib.returnbook(book)
#    else:
#        print("not a valid choice")
#    print("="*60)

#    print("enter q to exist and c to continue")
#    ch=""
#    while(ch != "c" and ch != "q"):
#        ch = input()
#        if(ch=="q"):
#            exit()
#        elif(ch=="c"):
#            continue













