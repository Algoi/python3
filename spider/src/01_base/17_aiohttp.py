# uv add aiohttp
import re
import aiohttp
import asyncio

async def first():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://httpbin.org/get') as resp:
            print(resp.status)
            print(await resp.text())


header = {'User-Agent': '123'}
# 两个地方都可以放请求头
async def test_headers():
    async with aiohttp.ClientSession(headers=header) as session:
        async with session.get('http://httpbin.org/headers', headers=header) as resp:
            print(resp.status)
            print(await resp.text())

async def test_param():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://httpbin.org/get', params={'a': 1, 'b': 2}) as resp:
            print(resp.status)
            print(await resp.text())

async def test_cookies():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://httpbin.org/cookies', cookies={'a': 1, 'b': 2}) as resp:
            print(resp.status)
            print(await resp.text())


async def spider(url, session):
    async with session.get(url) as resp:
        data = await resp.json()
        page = re.findall(r'page=(\d+)', url)
        print(f'第{page}页数据的总数为{len(data.get('items'))}')

async def main():
    url_list = [f'http://58.87.96.193:8000/api/movies?page={i}&movie_type=&movie_time=' for i in range(1, 11)]
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(spider(url, session)) for url in url_list]
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    # python < 3.14
    # loop = asyncio.get_event_loop()
    # loop.run(first())

    # python >= 3.14
    # asyncio.run(first())
    # asyncio.run(test_headers())
    # asyncio.run(test_param())
    # asyncio.run(test_cookies())

    asyncio.run(main())
