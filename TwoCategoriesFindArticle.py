import requests
import random

S = requests.Session()
url = "https://en.wikipedia.org/w/api.php"

def getSubcategories(category):
    params = {
        "action": "query",
        "cmtitle": category,
        "cmtype": "subcat",
        "cmlimit": "max",
        "list": "categorymembers",
        "format": "json"
    }

    data = S.get(url=url, params=params).json()
    if 'query' in data.keys():
        return data['query']['categorymembers']
    else:
        return []

def getArticles(category):
    params = {
        "action": "query",
        "cmtitle": category,
        "cmtype": "page",
        "cmlimit": "max",
        "list": "categorymembers",
        "format": "json"
    }

    data = S.get(url=url, params=params).json()
    if 'query' in data.keys():
        return data['query']['categorymembers']
    else:
        return []

def getCategoriesOfPage(page):
    params = {
        "action": "query",
        "prop": "categories",
        "titles": page['title'],
        "cllimit": "max",
        "clshow": "!hidden",
        "format": "json"
    }

    data = S.get(url=url, params=params).json()
    if 'query' in data.keys():
        return [category['title'] for category in list(data['query']['pages'].values())[0]['categories']]
    else:
        return []



def selectRandomArticle(category):
    articles = getArticles(category)
    if articles != []:
        return random.choice(articles)
    return None



def findArticle(category1, category2):
    l1, l2 = set([category1]), set([category2])
    s1 = getSubcategories(category1)
    s2 = getSubcategories(category2)
    for category in s1:
        l1.add(category['title'])
    for category in s2:
        l2.add(category['title'])

    articles1, articles2 = getArticles(category1), getArticles(category2)

    matches = {}
    for article in articles1:
        articleCategories = getCategoriesOfPage(article)
        for category in articleCategories:
            if category in l2:
                matches[article['title']] = article

    for article in articles2:
        articleCategories = getCategoriesOfPage(article)
        for category in articleCategories:
            if category in l1:
                matches[article['title']] = article


    return matches
    #
    #
    # l1 += getSubcategories(category1)
    # l2 += getSubcategories(category2)
    # page = None
    # depth = 0
    #
    # while len(searchResults) > 0:
    #     page = random.choice(searchResults)
    #     print(page)
    #     category = page['title']
    #     searchResults = getSubcategories(category)
    #     depth += 1
    #     if random.random() > 1.0/(depth + 1):
    #         article = selectRandomArticle(category)
    #         if (article != None):
    #             return article
    #
    # return selectRandomArticle(category)

print(findArticle("Category:Concepts in physics","Category:Systems theory"))
