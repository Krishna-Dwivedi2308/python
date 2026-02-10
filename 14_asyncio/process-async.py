import asyncio
from concurrent.futures import ProcessPoolExecutor


def encrypt_data(data):
    return f"Encrypted {data[::-1]}"


async def main():
    loop = asyncio.get_running_loop()  # running loop for the threds
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, encrypt_data, "masala chai")
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
