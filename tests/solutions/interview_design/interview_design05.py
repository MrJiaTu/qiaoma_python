import threading

class Inventory:
    def __init__(self, stock):
        self.stock = stock
        self.lock = threading.Lock()

    def buy(self):
        with self.lock:
            if self.stock > 0:
                self.stock -= 1
                return True
            return False
