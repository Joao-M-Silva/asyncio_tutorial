import asyncio

async def waiter(event: asyncio.Event):
    print("Waiting for the event to be set")
    await event.wait()
    print("Event has been set. Continuing ...")

async def setter(event: asyncio.Event):
    print("Inside setter")
    await asyncio.sleep(2)
    event.set()
    print("Event has been set")

async def main():
    event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))

asyncio.run(main())