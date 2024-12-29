"""
asyncio.gather is a quick way to run multiple coroutines concurrently 

Note: using gather struggles with error handling, not cancelling all coroutines 
if a single one fails
"""

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
    task3 = fetch_data(delay, 3)

    results = await asyncio.gather(task1, task2, task3)
    print("Results: ", results)
    
    print("End of main coroutine")

asyncio.run(main(2))