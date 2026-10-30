# ============================================================
# async 异步编程 08 · 异步生成器分批推单
# ============================================================
# 【场景】调度系统分批推送订单，用 async for 消费。
# 【任务】修复 push_orders 异步生成器。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
import asyncio

async def push_orders():
    for batch in (["A1", "A2"], ["B1"]):
        await asyncio.sleep(0.01)
        return batch  # return 只会产出一次

async def main():
    got = []
    async for batch in push_orders():
        got.extend(batch)
    return got

orders = asyncio.run(main())
