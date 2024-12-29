"""
Preferred way to run multiple coroutines concurrently.
If a task inside a task group fails it automatically cancels all the other tasks
"""

import asyncio


async def fetch_data(delay: int, id: int):
    print("Fetching data ... id: ", id)
    await asyncio.sleep(delay)
    print("Data fetched, id: ", id)
    return {"data": "some data", "id": id}

async def main():
    print("Start of main coroutine")
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i, delay in enumerate([1, 2, 1]):
            task = tg.create_task(fetch_data(delay, i))
            tasks.append(task)
        
        print("All tasks created")

    # Once here, all the tasks above were already executed
    print("All tasks executed")

    results = [task.result() for task in tasks]
    print("Results: ", results)
    
    print("End of main coroutine")

asyncio.run(main())