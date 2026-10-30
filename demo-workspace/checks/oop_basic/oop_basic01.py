assert book.title == "西游记", f"书名没存上：{getattr(book, 'title', None)}"
