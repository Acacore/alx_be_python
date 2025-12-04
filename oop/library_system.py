

class Book:
    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author
    def __str__(self):
        return f"{self.title} {self.author}"
    

class EBook(Book):
    def __init__(self, title, author):
        super().__init__(title, author)
    
    def file_size (self, file_size:int=0):
        self.file_size = file_size

    def __str__(self):
        return f"{self.title} by {self.author}, File Size: {self.file_size}MB"

class PrintBook(Book):
    def __init__(self, title, author):
        super().__init__(title, author)

    def page_count(self, page_count:int=0):
        self.page_count = page_count

    def __str__(self):
        return f"{self.title} by {self.author}, File Size: {self.page_count}"

    

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book.title, book.author) 
        
    