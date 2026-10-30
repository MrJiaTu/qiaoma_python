def read_lines(path):
    with open(path, encoding="utf-8") as f:
        for line in f:
            yield line

with open("log.txt", "w", encoding="utf-8") as f:
    f.write("a\nb\nc\n")
result = list(read_lines("log.txt"))
