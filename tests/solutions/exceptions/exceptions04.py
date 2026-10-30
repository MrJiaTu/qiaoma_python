logged = False
try:
    transfer = 100 / 0
except ZeroDivisionError:
    pass
finally:
    logged = True
