results = [False, False, True]
success = False
attempts = 0
for ok in results:
    attempts = attempts + 1
    if ok:
        success = True
        break
