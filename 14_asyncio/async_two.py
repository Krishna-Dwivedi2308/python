import asyncio
import time


async def brew(name):
    print(f"Brewing {name}...")
    await asyncio.sleep(3)
    print(f"{name} is ready")


async def main():
    start = time.time()
    await asyncio.gather(brew("Masala Chai"), brew("Green Chai"), brew("Ginger chai"))
    end = time.time()
    print(f"Took {end-start:.2f}")
    # Took 3.01 seconds - but if await waits for execution then how did it take 3 secs only ? => because it does it in a non blocking way .


if __name__ == "__main__":
    asyncio.run(main())

# This property of non-blocking makes things like fastapi very fast.
