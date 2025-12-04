

class Book:
    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author):
        super().__init__(title, author)
    
    def file_size (self, int):
        ...

class PrintBook(Book):
    def __init__(self, title, author):
        super().__init__(title, author)
    def page_count(self, int):
        ...
    

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book.title, book.author) 
        
    