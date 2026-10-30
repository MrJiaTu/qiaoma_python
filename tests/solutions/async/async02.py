import asyncio

async def cook():
    return "黄焖鸡"

async def fetch_meal():
    meal = await cook()
    return meal

result = asyncio.run(fetch_meal())
