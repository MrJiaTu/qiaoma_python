# ============================================================
# 面向对象入门 08 · 电子书下载
# ============================================================
# 【场景】电子书的 borrow 含义不同：借即下载，要重写方法。
# 【任务】在 EBook 中重写 borrow，设置 downloaded。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
class Book:
    def __init__(self, title):
        self.title = title

    def borrow(self):
        self.is_borrowed = True

class EBook(Book):
    def __init__(self, title):
        super().__init__(title)
        self.downloaded = False
    # 缺少重写的 borrow

eb = EBook("三体")
eb.borrow()
