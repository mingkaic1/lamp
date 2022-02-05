# import wikipedia
#
# searchResults = wikipedia.search("hello")
# page = wikipedia.page(searchResults[0],auto_suggest=False)
# print(page.links)

import requests

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
    pages = data['query']['categorymembers']

    return pages

category = "Category:Physics"
searchResults = searchCategory(category)
while len(searchResults) > 0:
    category = random(searchResults)
    searchResults = searchCategory(category)
print(category)
