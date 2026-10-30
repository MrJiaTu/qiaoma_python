import threading

done = []

def download():
    done.append("完成")

t = threading.Thread(target=download)
t.start()
t.join()
