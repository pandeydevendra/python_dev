import json
import requests


def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain. The grader will supply the URL as an argument to
    # the function; you do not need to construct the address or call this
    # function in your grader submission.
    #

    data_url = requests.get(url).text
    data = json.loads(data_url)

    # Once you've done this, return the name of the number 1 top artist in
    # Spain.
    spain_artist = data['topartists']['artist'][0]['name']
    # return the top artist in Spain

    return spain_artist  # return the top artist in Spain


url = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=4beab33cc6d65b05800d51f5e83bde1b&format=json'
top_artist = api_get_request(url)
print(top_artist)

#  Good job! Arctic Monkeys is top artist in Spain
