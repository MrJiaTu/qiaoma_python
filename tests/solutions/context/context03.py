from contextlib import contextmanager

events = []

@contextmanager
def work_session():
    events.append("开工")
    try:
        yield
    finally:
        events.append("收工")

with work_session():
    events.append("干活")
