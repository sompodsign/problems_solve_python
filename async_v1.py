import asyncio


async def function_async():
    for i in range(50000):
        print("Hello I'm Shampad")
        print("I'm great")
        # await asyncio.sleep(0.01)
    return 0


async def function_2():
    print("\n HELLO WORLD \n")
    return 0


async def main():
    f1 = loop.create_task(function_async())
    f2 = loop.create_task(function_2())
    await asyncio.wait([f1, f2])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
