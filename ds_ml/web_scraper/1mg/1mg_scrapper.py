import requests
from bs4 import BeautifulSoup as soup
import pandas as pd

# Define header:
header = {'Origin': 'https://www.1mg.com',
          'Referer': 'https://www.1mg.com/categories/exclusive/immunity-boosters/vitamin-c-734',
          'User-Agent': 'new_web_user'}

# Send a get request:
url = 'https://www.1mg.com/categories/exclusive/immunity-boosters/vitamin-c-734'
html = requests.get(url=url, headers=header)
bsobj = soup(html.content, 'html.parser')

# Get product name:
product_name = []
for name in bsobj.findAll('div', {'itemprop': 'name'}):
    product_name.append(name.text.strip())

print(product_name)
