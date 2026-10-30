config = {"host": "127.0.0.1"}
try:
    timeout = config["timeout"]
except KeyError:
    timeout = 30
