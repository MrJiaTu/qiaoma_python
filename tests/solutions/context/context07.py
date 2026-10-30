import os
import shutil

class TempDir:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        os.makedirs(self.path, exist_ok=True)
        return self.path

    def __exit__(self, exc_type, exc, tb):
        shutil.rmtree(self.path, ignore_errors=True)

with TempDir("tmp_build") as p:
    open(os.path.join(p, "a.txt"), "w").write("x")
cleaned = not os.path.exists("tmp_build")
