with open("signup.txt", "w", encoding="utf-8") as f:
    f.write("王芳\n刘强\n")
names = []
with open("signup.txt", encoding="utf-8") as f:
    for line in f:
        names.append(line.strip())
