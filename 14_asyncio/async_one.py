# This code depicts the working of asyncio
import asyncio


async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


asyncio.run(main())
# coroutines , event loop , tasks , futures
