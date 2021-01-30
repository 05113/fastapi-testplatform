import time
import asyncio

async def a():
    start = time.time()
    print(start,'a')
    time.sleep(3)
    print('aa',time.time())
    await b()
    print('a',time.time())

async def b():
    start1 = time.time()
    print(start1,'b')
    await asyncio.sleep(10)
    print('b',time.time())


async def main():
    await a()

asyncio.get_event_loop().run_until_complete(main())