# ============================================================
# async 异步编程 04 · create_task 边做菜边接单
# ============================================================
# 【场景】厨房开始做菜后，前台同时接单，最后一起收尾。
# 【任务】用 create_task 把做菜丢到后台。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
import asyncio

events = []

async def cook():
    await asyncio.sleep(0.02)
    events.append("菜好了")

async def take_order():
    events.append("接单")

async def main():
    await cook()  # 阻塞等菜做完才接单
    await take_order()

asyncio.run(main())
