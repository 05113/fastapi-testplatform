import asyncio
import time
async def nested():  # async def定义一个协程函数，调用它返回的是协程对象
    time.sleep(1)
    return 42

async def main():
    # 直接运行nested()不会得到任何结果，这位这是一个协程对象（协程对象：调用协程函数所返回的对象）
#     nested()

    # await 后面接的是协程，所以他是一个可等待对象，因此可以在其他协程中被等待
    print(1)
    print(await nested())  # will print "42".
    print(2)
# asyncio.run(main())  # asyncio.run()运行一个协程
asyncio.get_event_loop().run_until_complete(main())
