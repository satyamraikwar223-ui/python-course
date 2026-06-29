import time
import asyncio

async def function1():
    await asyncio.sleep(1)
    print("funt 1")
    return "satyam"

async def function2():
    await asyncio.sleep(1)
    print("func 2")

async def function3():
    await asyncio.sleep(4)
    print("func 3")

async def main():
    L = await asyncio.gather(
       function1(),
       function2(),
       function3()
    )
    
    print(L)
    #task = async.create_task(function())
    #await function1()
    #await function2()
    #await function3()

asyncio.run(main())