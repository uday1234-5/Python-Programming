class LibraryBook:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(f"{self.title} by {self.author} has been successfully borrowed.")
        else:
            print(f"Sorry, {self.title} by {self.author} is currently unavailable.")
    def return_book(self):
        self.is_available = True
        print(f"{self.title} by {self.author} has been returned and is now available.")
    def __str__(self):
        availability = "Available" if self.is_available else "Unavailable"
        return f"Title: {self.title}, Author: {self.author}, Status: {availability}"
# Example Usage
book = LibraryBook("Concepts of Physics", "H.C. verma")
print(book)
book.borrow_book()
print(book)
book.return_book()
print(book)