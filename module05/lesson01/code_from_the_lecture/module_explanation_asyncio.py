"""This code is from lectures"""

import asyncio
from time import sleep, time

# Example 1 How to use async await
async def baz() -> str:
    print('Before sleep')
    await asyncio.sleep(1)  # Not blocking operation sleep
    print('After sleep')
    return 'Hello python developers'

async def main():
    r = baz()
    print(r)
    result = await r
    print(result)



# Example 2 compare async code with sync.
fake_users = [
    {'id': 1, 'name': 'April Murphy', 'company': 'Bailey Inc', 'email': 'shawnlittle@example.org'},
    {'id': 2, 'name': 'Emily Alexander', 'company': 'Martinez-Smith', 'email': 'turnerandrew@example.org'},
    {'id': 3, 'name': 'Patrick Jones', 'company': 'Young, Pruitt and Miller', 'email': 'alancoleman@example.net'}
]
def get_user_sync(uid: int) -> dict:
    sleep(0.5)
    user, = list(filter(lambda user: user["id"] == uid, fake_users))
    return user

# Example 3 the same but with async code
async def get_user_async(uid: int) -> dict:
    await asyncio.sleep(0.5)  # not blocking operation
    user, = list(filter(lambda user: user["id"] == uid, fake_users))
    return user


async def main():
    r = []
    for i in range(1, 4):
        r.append(get_user_async(i))
    return await asyncio.gather(*r)  # gather for run few subprograms running concurently and in a strict que.

if __name__ == '__main__':
    # Example 1
    # asyncio.run(main())

    # Example 2
    # start = time()
    # for i in range(1, 4):
    #     print(get_user_sync(i))
    # print(time() - start)

    # Example 3
    start = time()
    result = asyncio.run(main())  # run create Event loop and put coroutine into the que. When the que is empty finish Event loop
    for r in result:
        print(r)
    print(time() - start)