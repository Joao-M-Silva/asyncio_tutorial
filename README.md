# Python Asyncio Tutorial
This repository is a simple asyncio tutorial. Asyncio is a python stardard library used to write concurrent code using the async/await syntax.
Running code concurrently is beneficial since it allows to start running some code even though some previous task is not finished yet. 
Please note that asynchronicity is single threaded and don't use multiple CPU cores. We are not executing multiple tasks in parallel, which is the case for multihreading and multiprocessing. 

## When to use asyncio
Everytime that we want to run multiple tasks that need to wait a lot independently of the program being executed. 

## Event loop
An event loop manages and distributes tasks. Each single task waits for their turn to be executed immediatly or paused if its waiting for something like data from the internet. When a task awaits , it steps aside making room for another task to run, ensuring that the loop is always efficiently utilized. Once the awaited operation is complete, the task will resume.

Note: use python```asyncio.run()``` to start an event loop.
