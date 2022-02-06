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

def selectRandomArticle(category):
    params = {
        "action": "query",
        "cmtitle": category,
        "cmtype": "page",
        "cmlimit": "20",
        "list": "categorymembers",
        "format": "json"
    }

    data = S.get(url=url, params=params).json()
    if 'query' in data.keys():
        pages = data['query']['categorymembers']
    else:
        pages = []

    if pages != []:
        return random.choice(pages)
    return None



def findArticle(category):
    searchResults = searchCategory(category)
    page = None
    depth = 0

    while len(searchResults) > 0:
        page = random.choice(searchResults)
        print(page)
        category = page['title']
        searchResults = searchCategory(category)
        depth += 1
        if random.random() > 1.0/(depth + 1):
            article = selectRandomArticle(category)
            if (article != None):
                return article

    return selectRandomArticle(category)

print(findArticle("Category:Physics"))
