import asyncio

shared_resource = 0

lock = asyncio.Lock()

async def modify_shared_resource(id):
    global shared_resource
    print("Executing task ", id)
    async with lock:
        # All this code needs to be executed for the lock to be released
        print("Resource before modification: ", shared_resource, "id: ", id)
        shared_resource += 1
        await asyncio.sleep(2) 
        print("Resource after modification: ", shared_resource, "id: ", id)
        print("Lock released")

async def main():
    await asyncio.gather(*(modify_shared_resource(i) for i in range(5)))

asyncio.run(main())