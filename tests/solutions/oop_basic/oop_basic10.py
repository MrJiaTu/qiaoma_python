class Book:
    def late_fee(self, days):
        return days * 0.5

book = Book()
fee = book.late_fee(3)
