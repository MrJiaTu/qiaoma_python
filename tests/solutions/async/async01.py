import asyncio

async def greet():
    return "你好，外卖平台"

result = asyncio.run(greet())
