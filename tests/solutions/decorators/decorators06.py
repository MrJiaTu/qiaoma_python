def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == times - 1:
                        raise
        return wrapper
    return decorator

attempts = []

@retry(3)
def unstable():
    attempts.append(1)
    if len(attempts) < 3:
        raise ConnectionError("网络抖动")
    return "成功"

result = unstable()
