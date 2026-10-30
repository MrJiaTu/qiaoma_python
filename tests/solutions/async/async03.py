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
    return await asyncio.gather(deliver("骑手A"), deliver("骑手B"))

results = asyncio.run(main())
