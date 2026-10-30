# ============================================================
# async 异步编程 03 · gather 并发派单
# ============================================================
# 【场景】两个骑手同时出发派单，用 gather 并发执行并记录并发数。
# 【任务】修复代码：用 asyncio.gather 并发跑两个协程。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
import asyncio

active = 0
peak = 0

async def deliver(name):
    global active, peak
    active += 1
    peak = max(peak, active)
    await asyncio.sleep(0.02)
    active -= 1
    return f"{name}已送达"

async def main():
    r1 = await deliver("骑手A")  # 串行等待
    r2 = await deliver("骑手B")
    return [r1, r2]

results = asyncio.run(main())
