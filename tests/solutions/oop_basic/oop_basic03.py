class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"《{self.title}》"

book = Book("西游记")
info = str(book)
