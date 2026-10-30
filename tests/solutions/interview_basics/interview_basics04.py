def make_funcs():
    funcs = []
    for i in range(3):
        funcs.append(lambda i=i: i)
    return funcs

f0, f1, f2 = make_funcs()
results = [f0(), f1(), f2()]
