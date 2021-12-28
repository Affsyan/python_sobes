import aiofiles
import aiohttp
import asyncio


URLS = ['http://127.0.0.1:8000/', 'http://127.0.0.1:8000/category', 'http://127.0.0.1:8000/admin']


async def fetch_async(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.text()


async def main(url):
    content = await fetch_async(url)
    fname = url.split("/")[-1]
    async with aiofiles.open(f'{fname}.txt', 'w', encoding='utf-8') as f:
        await f.write(content)

futures = [main(url) for url in URLS]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))
