# ============================================================
# async 异步编程 05 · wait_for 超时兜底
# ============================================================
# 【场景】骑手 0.05 秒才能送达，平台只等 0.01 秒，超时要给用户提示。
# 【任务】用 asyncio.wait_for 捕获超时。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
import asyncio

async def slow_deliver():
    await asyncio.sleep(0.05)
    return "已送达"

async def main():
    return await slow_deliver()  # 没设超时

result = asyncio.run(main())
