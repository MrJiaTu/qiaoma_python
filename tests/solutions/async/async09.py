import asyncio

async def producer(q):
    for i in range(3):
        await q.put(f"订单{i}")

async def consumer(q):
    taken = []
    while not q.empty():
        taken.append(await q.get())
    return taken

async def main():
    q = asyncio.Queue()
    await producer(q)
    return await consumer(q)

taken = asyncio.run(main())
