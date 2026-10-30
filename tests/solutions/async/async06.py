import asyncio

async def make(name, delay):
    await asyncio.sleep(delay)
    return name

async def main():
    jobs = [make("快餐店", 0.03), make("面馆", 0.01)]
    order = []
    for coro in asyncio.as_completed(jobs):
        order.append(await coro)
    return order

order = asyncio.run(main())
