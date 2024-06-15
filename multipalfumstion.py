import time 
import asyncio
async def fun1( ):
    await asyncio.sleep(1)
    print('fun1')
async def fun2 ( ):
    await asyncio.sleep(1)
    print('fun2')
async def fun3 ( ):
    await asyncio.sleep(1)
    print('fun3')
async def fun4 ( ):
    await asyncio.sleep(1)
    print('fun4')

async def main():
    l = await asyncio.gather(
         fun1(),
         fun2(),
         fun3(),
         fun4()
    )
asyncio.run(main())