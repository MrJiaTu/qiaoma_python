stock = [("键盘", 3), ("鼠标", 0), ("音箱", 5)]
available = list(filter(lambda item: item[1] > 0, stock))
