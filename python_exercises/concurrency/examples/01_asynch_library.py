import asyncio  # import the std for asynch
import time


async def task(delay, what):  # define task as manageable by asychio
    await asyncio.sleep(delay)  # sleep
    print(what)


async def main():
    now = time.time()
    task1 = asyncio.create_task(
        task(10, '1 - 10 sec'))
    task2 = asyncio.create_task(
        task(20, '2 - 20 sec'))
    await task1  # join
    await task2
    print(f"total: {time.time() - now}")


asyncio.run(main())
