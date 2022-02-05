# import wikipedia
#
# searchResults = wikipedia.search("hello")
# page = wikipedia.page(searchResults[0],auto_suggest=False)
# print(page.links)

import requests
import random

S = requests.Session()
url = "https://en.wikipedia.org/w/api.php"

def searchCategory(category):
    params = {
        "action": "query",
        "cmtitle": category,
        "cmtype": "subcat",
        "cmlimit": "20",
        "list": "categorymembers",
        "format": "json"
    }

    data = S.get(url=url, params=params).json()
    if 'query' in data.keys():
        pages = data['query']['categorymembers']
    else:
        pages = []

    return pages

category = "Category:Physics"
searchResults = searchCategory(category)
page = None

while len(searchResults) > 0:
    page = random.choice(searchResults)
    print(page)
    category = page['title']
    searchResults = searchCategory(category)

# print(page)
