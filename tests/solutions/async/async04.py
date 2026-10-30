import asyncio

events = []

async def cook():
    await asyncio.sleep(0.02)
    events.append("菜好了")

async def take_order():
    events.append("接单")

async def main():
    task = asyncio.create_task(cook())
    await take_order()
    await task

asyncio.run(main())
