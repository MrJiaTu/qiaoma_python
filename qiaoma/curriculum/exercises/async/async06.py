# ============================================================
# async 异步编程 06 · as_completed 先做先得
# ============================================================
# 【场景】两家餐厅同时出餐，谁先好先配送谁。
# 【任务】用 as_completed 按完成顺序收集结果。
# 【完成】修好后删除文件里的未完成标记行。
# ============================================================

# 我还没做完
import asyncio

async def make(name, delay):
    await asyncio.sleep(delay)
    return name

async def main():
    jobs = [make("快餐店", 0.03), make("面馆", 0.01)]
    results = await asyncio.gather(*jobs)  # gather 是按提交顺序
    return results

order = asyncio.run(main())
