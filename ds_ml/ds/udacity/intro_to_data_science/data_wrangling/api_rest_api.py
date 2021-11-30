import json
import requests


def api_get_request(url):
    data_url = requests.get(url).text
    # data = json.loads(data_url)

    return data_url


dataset_result = api_get_request('https://www.last.fm/api/show/album.getInfo')  # write right url
print(dataset_result)