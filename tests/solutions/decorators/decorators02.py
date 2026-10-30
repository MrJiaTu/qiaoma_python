logged_in = False

def login_required(func):
    def wrapper():
        if not logged_in:
            return "请先登录"
        return func()
    return wrapper

@login_required
def profile():
    return "李雷的资料"

result = profile()
