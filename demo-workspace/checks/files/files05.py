assert closed is True, "离开 with 块后文件应自动关闭"
assert open("note.txt", encoding="utf-8").read() == "记得带伞"
