import asyncio

async def task():
    print("Task started")
    await asyncio.sleep(3)   # non-blocking wait
    print("Task finished")

async def main():
    await task()
    print("Program end")

asyncio.run(main())
# This code demonstrates the use of asyncio to run an asynchronous task.

'''
Important Keywords (Easy Words)

async def → async function

await → wait but don’t block

asyncio.sleep() → non-blocking sleep

asyncio.run() → async program start

asyncio.gather() → multiple tasks together

'''