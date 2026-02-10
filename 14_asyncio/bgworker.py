import asyncio
import threading
import time


def background_worker():
    while True:
        print("Background worker is working...")
        time.sleep(1)
        print("Logging the system health...👨🏻‍⚕️")


async def fetch_orders():
    await asyncio.sleep(3)
    print("Fetched all orders")


threading.Thread(target=background_worker, daemon=True).start()
asyncio.run(fetch_orders())
