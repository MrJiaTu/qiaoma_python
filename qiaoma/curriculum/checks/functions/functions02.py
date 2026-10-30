assert msg == "中秋快乐，尊敬的客户！", f"没传参时应使用默认称呼：{msg}"
assert greet("李雷") == "中秋快乐，李雷！"
