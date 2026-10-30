# ============================================================
# 上下文管理器 07 · 临时目录上下文
# ============================================================
# 【场景】打包临时文件，用完整个目录要自动清理。
# 【任务】实现 TempDir：进入时创建，退出时清理。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
import os
import shutil

class TempDir:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        os.makedirs(self.path, exist_ok=True)
        return self.path

    def __exit__(self, exc_type, exc, tb):
        pass  # 没清理

with TempDir("tmp_build") as p:
    open(os.path.join(p, "a.txt"), "w").write("x")
cleaned = not os.path.exists("tmp_build")
