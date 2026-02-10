import asyncio
import aiohttp
import time


async def fetch_url(session, url):
    async with session.get(url) as response:
        print(response.url)


async def main():
    start = time.time()
    urls = ["https://httpbin.org/delay/2"] * 3
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        # tasks=[t1,t2,t3]
        await asyncio.gather(
            *tasks
        )  # here * unpacks all the elements in the array inside the parentheses  - just like the (...)spread operator in python
    end = time.time()
    print(f"Fetched all apis in {end-start:.2f}")  # takes 3.8 seconds
    # but if it were blocking , it should have taken 6 secs


asyncio.run(main())
