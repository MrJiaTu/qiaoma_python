class Library:
    def __init__(self):
        self.books = ["西游记", "水浒传", "红楼梦"]

    def count_books(self):
        return len(self.books)

lib = Library()
count = lib.count_books()
