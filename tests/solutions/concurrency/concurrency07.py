import threading

local = threading.local()
seen = {}

def handle(name):
    local.user = name
    seen[name] = local.user

t1 = threading.Thread(target=handle, args=("张三",))
t2 = threading.Thread(target=handle, args=("李四",))
t1.start(); t2.start(); t1.join(); t2.join()
