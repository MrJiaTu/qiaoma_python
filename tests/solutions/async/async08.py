import asyncio

async def push_orders():
    for batch in (["A1", "A2"], ["B1"]):
        await asyncio.sleep(0.01)
        yield batch

async def main():
    got = []
    async for batch in push_orders():
        got.extend(batch)
    return got

orders = asyncio.run(main())
