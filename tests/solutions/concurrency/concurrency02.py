import threading

pages = []

def crawl(name):
    pages.append(name)

threads = [threading.Thread(target=crawl, args=(f"页{i}",)) for i in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()
count = len(pages)
