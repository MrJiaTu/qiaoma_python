# ============================================================
# 上下文管理器 08 · closing 关闭老接口
# ============================================================
# 【场景】老版本爬虫对象没有 __exit__，只有 close()，要用 closing 包一下。
# 【任务】用 contextlib.closing 保证 close 被调用。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
from contextlib import closing

class OldSpider:
    def __init__(self):
        self.closed = False

    def close(self):
        self.closed = True

spider = OldSpider()
spider.close  # 引用了但没调用，也没用 with
