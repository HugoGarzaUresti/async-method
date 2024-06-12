import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def async_task(name, url):
    print(f'Task {name} started')
    async with aiohttp.ClientSession() as session:
        content = await fetch_url(session, url)
        print(f'Task {name} completed with content length {len(content)}')

async def main():
    urls = [
        ('A', 'https://www.example.com'),
        ('B', 'https://www.example.org'),
        ('C', 'https://www.example.net'),
    ]
    await asyncio.gather(*(async_task(name, url) for name, url in urls))

if __name__ == "__main__":
    asyncio.run(main())
