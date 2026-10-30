def squares_gen():
    return (n * n for n in range(3))

first = list(squares_gen())
second = list(squares_gen())
