status = None

class Room:
    def __enter__(self):
        global status
        status = "使用中"
        return self

    def __exit__(self, exc_type, exc, tb):
        global status
        status = "空闲"

with Room():
    pass
