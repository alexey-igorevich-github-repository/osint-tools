import asyncio
from requests_html import AsyncHTMLSession
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)

async def get_all_website_links(url, session):
    urls = set()
    domain_name = urlparse(url).netloc
    try:
        response = await session.get(url, timeout=max_parsing_time)
        await response.html.arender(timeout=max_parsing_time)
    except Exception as e:
        logging.error(f"Error rendering {url}: {e}, Status Code: {response.status_code if 'response' in locals() else 'Unknown'}")
        return urls

    soup = BeautifulSoup(response.html.html, "html.parser").findAll("a")
    for tag_a in soup:
        href = tag_a.attrs.get("href")

        if href is None or href == "":
            continue

        href = urljoin(url, href)
        parsed_href = urlparse(href)
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path

        if href in INTERNAL_URLS:
            continue
        if domain_name not in href:
            if href not in EXTERNAL_URLS:
                logging.info(f"[*] External link: {href}")
                EXTERNAL_URLS.add(href)
            continue
        logging.info(f" [*] Internal link: {href}")
        urls.add(href)
        INTERNAL_URLS.add(href)
    return urls

async def crawl(url, current_depth, max_depth):
    if current_depth == max_depth:
        return


    logging.info(f"[*] Crawling: {url}, Depth: {current_depth}")
    session =  AsyncHTMLSession()
    try:
        links = await get_all_website_links(url, session)
        tasks = [crawl(link, current_depth + 1, max_depth) for link in links]
        await asyncio.gather(*tasks)
    finally:
        await session.close()

if __name__ == "__main__":
    INTERNAL_URLS = set()
    EXTERNAL_URLS = set()

    start_url = input("Please type or paste your link to crawl through in this format https://www.scrapethissite.com  >>> ")
    current_depth = 0
    max_depth = input("Please input maximum crawl depth >>> ")
    max_parsing_time = int(input("Please input maximum wait-time to parse single link >>> "))
    asyncio.run(crawl(start_url, current_depth, max_depth))

    with open("links.txt", "w") as f:
        print('INTERNAL:', file=f)
        for internal_link in INTERNAL_URLS:
            print(internal_link.strip(), file=f)
        print('EXTERNAL:', file=f)
        for external_link in EXTERNAL_URLS:
            print(external_link.strip(), file=f)

