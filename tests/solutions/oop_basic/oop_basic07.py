class Book:
    def __init__(self, title):
        self.title = title

class EBook(Book):
    def __init__(self, title, fmt):
        super().__init__(title)
        self.fmt = fmt

eb = EBook("三体", "epub")
