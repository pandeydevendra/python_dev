import time
import datetime
import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install beautifulsoup4
import pandas as pd

base_url = 'https://sfbay.craigslist.org/search/sfc/sya'

base_url = 'https://sfbay.craigslist.org/search/sfc/sya?s=120'

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}

# response
res = requests.get(url=base_url, headers=header)

# beautifulsoup object of the responce
soup = BeautifulSoup(res.content, 'html.parser')

# print(soup)

# print(soup.prettify())


# count all pages:
total_count = soup.find('span', 'totalcount').text

print(f"Total page count = {total_count}, {type(total_count)}")

total_results = int(total_count)
print(type(total_results))
# print all pages::(1-681)
