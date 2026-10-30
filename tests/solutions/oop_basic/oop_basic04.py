class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

lib = Library()
lib.add_book("西游记")
lib.add_book("水浒传")
