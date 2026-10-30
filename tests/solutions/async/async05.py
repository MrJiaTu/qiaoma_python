import asyncio

async def slow_deliver():
    await asyncio.sleep(0.05)
    return "已送达"

async def main():
    try:
        return await asyncio.wait_for(slow_deliver(), timeout=0.01)
    except (asyncio.TimeoutError, TimeoutError):
        return "超时改派"

result = asyncio.run(main())
