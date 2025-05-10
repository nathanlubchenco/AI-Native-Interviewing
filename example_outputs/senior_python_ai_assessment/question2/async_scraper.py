import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def scrape(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch(session, url)) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

if __name__ == "__main__":
    urls = ["https://example.com"] * 100
    results = asyncio.run(scrape(urls))
    print(f"Fetched {len(results)} pages")