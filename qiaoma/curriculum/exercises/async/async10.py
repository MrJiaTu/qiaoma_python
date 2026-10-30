# ============================================================
# async 异步编程 10 · 异步信号量限并发
# ============================================================
# 【场景】商家同时最多接 2 单，用 asyncio.Semaphore 限制。
# 【任务】在 handle 里用 async with sem 限流。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
import asyncio

sem = asyncio.Semaphore(2)
active = 0
peak = 0

async def handle(order):
    global active, peak
    active += 1  # 没走信号量
    peak = max(peak, active)
    await asyncio.sleep(0.02)
    active -= 1

async def main():
    await asyncio.gather(*(handle(i) for i in range(4)))

asyncio.run(main())
