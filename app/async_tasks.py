import asyncio

async def async_task(name, delay):
    print(f'Task {name} started')
    await asyncio.sleep(delay)
    print(f'Task {name} completed')

async def main():
    await asyncio.gather(
        async_task('A', 2),
        async_task('B', 1),
        async_task('C', 3)
    )
