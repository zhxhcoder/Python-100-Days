"""
异步I/O操作 - asyncio模块

Version: 0.1
Author: 团子
Date: 2018-03-21
"""

import asyncio
import threading


# import time

# 1.把@asyncio.coroutine替换为async；
# 2.把yield from替换为await。

async def hello():
    print('%s: hello, world!' % threading.current_thread())
    # 休眠不会阻塞主线程因为使用了异步I/O操作
    # 注意有await才会等待休眠操作执行完成
    await asyncio.sleep(2)
    # asyncio.sleep(1)
    # time.sleep(1)
    print('%s: goodbye, world!' % threading.current_thread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 等待两个异步I/O操作执行结束
loop.run_until_complete(asyncio.wait(tasks))
print('game over!')
loop.close()
