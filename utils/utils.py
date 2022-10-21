import requests
import asyncio
import aiohttp
from bs4 import BeautifulSoup

def get_multiple_html(urls):
    html_list = asyncio.run(get_async_htmls(urls))

    return html_list


async def get_async_htmls(urls):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(asyncio.create_task(read_url(session, url)))
        html_list = await asyncio.gather(*tasks)

    return html_list

async def read_url(session, url):
    
    try:
        async with session.get(url) as resp:
            html = await resp.text()
            soup = BeautifulSoup(html, 'html.parser')
            
            print("Finished url: " + url)

            return soup
    except Exception as e:
        print("Error in url: " + url)
        print(e)
        return None


def get_html(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    return soup
