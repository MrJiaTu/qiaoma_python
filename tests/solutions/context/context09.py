from contextlib import ExitStack

locks = {"A": False, "B": False}

def lock_bike(name):
    locks[name] = True

with ExitStack() as stack:
    for name in locks:
        stack.callback(lock_bike, name)
