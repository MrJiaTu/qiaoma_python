# ============================================================
# async 异步编程 02 · await 取餐
# ============================================================
# 【场景】在协程里调用另一个协程要 await。
# 【任务】修复 fetch_meal，让它 await 拿到结果。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
import asyncio

async def cook():
    return "黄焖鸡"

async def fetch_meal():
    meal = cook()  # 少了 await
    return meal

result = asyncio.run(fetch_meal())
