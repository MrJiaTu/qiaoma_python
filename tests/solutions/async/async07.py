import asyncio

events = []

class DeliveryBox:
    async def __aenter__(self):
        events.append("开箱")
        return self

    async def __aexit__(self, exc_type, exc, tb):
        events.append("锁箱")

async def main():
    async with DeliveryBox():
        events.append("放餐")

asyncio.run(main())
