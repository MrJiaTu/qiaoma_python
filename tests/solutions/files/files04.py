with open("checkin.txt", "w", encoding="utf-8") as f:
    f.write("张三\n李四\n王五\n")
with open("checkin.txt", encoding="utf-8") as f:
    count = len(f.readlines())
