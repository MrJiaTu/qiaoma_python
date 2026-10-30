import asyncio

sem = asyncio.Semaphore(2)
active = 0
peak = 0

async def handle(order):
    global active, peak
    async with sem:
        active += 1
        peak = max(peak, active)
        await asyncio.sleep(0.02)
        active -= 1

async def main():
    await asyncio.gather(*(handle(i) for i in range(4)))

asyncio.run(main())
