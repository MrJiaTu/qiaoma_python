# ============================================================
# async 异步编程 07 · 异步上下文管理器
# ============================================================
# 【场景】异步打开配送箱（async with），离开时自动上锁。
# 【任务】实现 __aenter__ 和 __aexit__。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
import asyncio

events = []

class DeliveryBox:
    async def __aenter__(self):
        events.append("开箱")
        return self
    # 缺少 __aexit__

async def main():
    async with DeliveryBox():
        events.append("放餐")

asyncio.run(main())
