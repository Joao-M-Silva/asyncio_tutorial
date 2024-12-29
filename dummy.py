""" No asynchronicity in this exemple since task 2 waits for task 1 to finish """

import asyncio


async def fetch_data(delay: int, id: int):
    print("Fetching data ... id: ", id)
    await asyncio.sleep(delay)
    print("Data fetched, id: ", id)
    return {"data": "some data", "id": id}

async def main(delay: int):
    print("Start of main coroutine")
    task1 = fetch_data(delay, 1)
    task2 = fetch_data(delay, 2)
    print(type(task1))
    print(type(task2))
    # Await the fetch data coroutine, pausing execution of
    # main until fetch_data completes
    result1 = await task1 # wait for the coroutine to finish
    print(f"Received result: {result1}")

    result2 = await task2 # wait for the coroutine to finish
    print(f"Received result: {result2}")
    print("End of main coroutine")

asyncio.run(main(2))