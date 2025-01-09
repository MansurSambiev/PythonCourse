import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнование')
    for i in range(5):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял шар {i + 1}')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Vanya', 5))
    task2 = asyncio.create_task(start_strongman('Vasya', 7))
    task3 = asyncio.create_task(start_strongman('Andre', 4))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())