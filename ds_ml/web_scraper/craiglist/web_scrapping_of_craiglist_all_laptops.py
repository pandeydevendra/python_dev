import datetime
import re
import time

import MySQLdb
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Open(set) database connection
web_db = MySQLdb.connect("localhost", "root", "root@123", "web_scrap_data", charset='latin1')

# prepare a cursor object using cursor() method
cursor = web_db.cursor()

FILE_PATH = '/home/vins/Workspace/Py/data_files/web_scrap/craiglist'

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}


def add_laptop_data(id, name, price, date, location, url):
    """
    this function will save laptop's data into table
    """
    print(f"\nData to be saved in the database:  {id}, {name}, {price}, {date}, {location}, {url}\n")
    name = re.sub('\W+', ' ', name)
    print(name)
    insert_in_product = f"""INSERT IGNORE INTO product_details 
                            SET product_id = '{id}', 
                            product_title = '{name}', 
                            product_price = '{price}', 
                            post_date = '{date}', 
                            location = '{location}',
                            post_url = '{url}'
                        """

    print(insert_in_product)
    cursor.execute(insert_in_product)
    web_db.commit()


def get_total_pages(base_url):
    response = requests.get(base_url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    total_results = int(soup.find('span', 'totalcount').text)
    print(f"total_results : {total_results}")
    total_pages = (total_results // 120) + 1
    print(f"total_pages : {total_pages}")
    return total_pages


def get_laptop_list(page_number, base_url):
    search_result_per_page = []
    params = {
        's': page_number * 120
    }

    print(f"params : {params}")
    print('Processing Page {0}'.format(page_number + 1))

    page_url = f"{base_url}?s={page_number * 120}"
    print(f"page_url : {page_url}")
    response = requests.get(page_url, headers=HEADERS)

    # continue
    soup = BeautifulSoup(response.content, 'html.parser')

    with open(f"{FILE_PATH}/1.html", 'w') as fp:
        fp.write(str(soup))

    results = soup.find('ul', {'id': 'search-results'})
    with open(f"{FILE_PATH}/2.html", 'w') as fp:
        fp.write(str(results))

    result_rows = results.find_all('li', 'result-row')
    with open(f"{FILE_PATH}/3.html", 'w') as fp:
        fp.write(str(result_rows))

    laptop_count = 0
    for result_row in result_rows:
        with open(f"{FILE_PATH}/4.html", 'w') as fp:
            fp.write(str(result_row))

        laptop_info = {}
        # import ipdb
        # ipdb.set_trace()
        laptop_count += 1
        # if laptop_count >= 2:
        #     break

        post_datetime = result_row.time['datetime']
        laptop_info['post_datetime'] = post_datetime
        post_id = result_row.h3.a['data-id']
        laptop_info['post_id'] = post_id
        post_url = result_row.h3.a['href']
        laptop_info['post_url'] = post_url
        price = result_row.find('span', 'result-price').text
        laptop_info['price'] = price
        location = result_row.find('span', 'result-hood').text if result_row.find('span', 'result-hood') else ''
        laptop_info['location'] = location
        post_title = result_row.h3.a.text
        laptop_info['post_title'] = post_title
        search_result_per_page.append([
            post_datetime, post_id, post_url, price, location, post_title
        ])

        add_laptop_data(post_id, post_title, price, post_datetime, location, post_url)
        print(laptop_info)

    return search_result_per_page


def main_program(base_url):
    search_results_all = []
    print(f"current_url : {base_url}")

    total_pages = get_total_pages(base_url)

    for page_number in range(0, total_pages):
        search_on_page_list = get_laptop_list(page_number, base_url)
        search_results_all.extend(search_on_page_list)
        time.sleep(1)

    columns = ('Post Date', 'Post Id', 'Post Url', 'Price', 'Location', 'Post title')
    df = pd.DataFrame(search_results_all, columns=columns)

    timestamp = datetime.datetime.now().strftime('%m_%d_%y %H%M%S')
    df.to_csv(f"{FILE_PATH}/craigslist_results_{timestamp}.csv", index=False)
    print('File Exported')


def main(query_url):
    try:
        main_program(query_url)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    url = 'https://sfbay.craigslist.org/search/sfc/sya'
    start_time = datetime.datetime.now()
    main(url)
    end_time = datetime.datetime.now()
    print(f"Total_run_time = {end_time - start_time}")