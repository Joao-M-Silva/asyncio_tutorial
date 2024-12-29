import asyncio

async def access_resource(semaphore: asyncio.Semaphore, id: int):
    print("Executing task ", id)
    async with semaphore:
        print("Accessing resource ", id)
        await asyncio.sleep(1)
        print("Releasing resource", id)

async def main():
    semaphore = asyncio.Semaphore(2) # allows 2 concurrent accesses
    await asyncio.gather(*(access_resource(semaphore, i) for i in range(5)))

asyncio.run(main())