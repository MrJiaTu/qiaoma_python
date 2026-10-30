with open("menu.txt", "w+", encoding="utf-8") as f:
    f.write("今日特价：宫保鸡丁")
    f.seek(0)
    text = f.read()
