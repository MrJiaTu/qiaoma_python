t = (1, [2, 3])
try:
    t[1].append(4)
    modified = False
except TypeError:
    modified = True

answer = "不会报错"
