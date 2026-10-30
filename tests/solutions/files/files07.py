import os

if not os.path.exists("health档案.txt"):
    status = "待建档"
else:
    status = "已建档"
