from concurrent.futures import ThreadPoolExecutor

def download(n):
    return f"图{n}"

with ThreadPoolExecutor(max_workers=2) as pool:
    results = list(pool.map(download, range(1, 6)))
