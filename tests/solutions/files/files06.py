with open("bill.csv", "w", encoding="utf-8") as f:
    f.write("牛奶,12.5\n面包,8.0\n")
total = 0
with open("bill.csv", encoding="utf-8") as f:
    for line in f:
        name, amount = line.strip().split(",")
        total = total + float(amount)
