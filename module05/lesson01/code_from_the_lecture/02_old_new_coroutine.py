import asyncio

@asyncio.coroutines
# def coroutine_my():
#     pass

# print(type(coroutine_my()))


    # yield from asyncio.sleep(1)

async def coroutine_my_new():
    await asyncio.sleep(1)  # From yield from to await. And magic method __await__()

print(type(coroutine_my_new()))  # <class 'coroutine'>

