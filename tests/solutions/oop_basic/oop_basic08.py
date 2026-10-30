class Book:
    def __init__(self, title):
        self.title = title

    def borrow(self):
        self.is_borrowed = True

class EBook(Book):
    def __init__(self, title):
        super().__init__(title)
        self.downloaded = False

    def borrow(self):
        super().borrow()
        self.downloaded = True

eb = EBook("三体")
eb.borrow()
