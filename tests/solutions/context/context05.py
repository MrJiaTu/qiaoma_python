import os
from contextlib import suppress

status = None
with suppress(FileNotFoundError):
    os.remove("不存在的缓存.tmp")
status = "忽略"
