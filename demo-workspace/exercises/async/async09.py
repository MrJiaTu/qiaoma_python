# ============================================================
# async 异步编程 09 · 异步队列生产消费
# ============================================================
# 【场景】接单系统生产订单，配送系统消费订单。
# 【任务】用 asyncio.Queue 传递三个订单。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
import asyncio

async def producer(q):
    for i in range(3):
        await q.put(f"订单{i}")

async def consumer(q):
    taken = []
    while not q.empty():
        taken.append(q.get_nowait())  # 同步方式取，先要保证生产完
    return taken

async def main():
    q = asyncio.Queue()
    await consumer(q)  # 先消费了，队列还是空的
    await producer(q)

taken = asyncio.run(main())
