import requests
import asyncio
from bs4 import BeautifulSoup


# def get_multiple_html(urls):
#     async def bar(i):
#         print('started', i)
#         await asyncio.sleep(1)
#         print('finished', i)

#     async def main():
#         await asyncio.gather(*[bar(i) for i in range(10)])

#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
#     loop.close()


def get_multiple_html(urls):
    pages = requests.get(urls)
    soup = BeautifulSoup(pages.content, 'html.parser')

    return soup


def get_html(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    return soup
