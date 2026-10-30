names = ["张三", "李四", "王五"]
with open("stars.txt", "w", encoding="utf-8") as f:
    f.writelines(name + "\n" for name in names)
