def average(scores):
    try:
        return sum(scores) / len(scores)
    except ZeroDivisionError:
        return 0

result = average([])
