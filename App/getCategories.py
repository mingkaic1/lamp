import requests

S = requests.Session()
url = "https://en.wikipedia.org/w/api.php"

def getSubCategories(category):
	"""
	Make API call to get all subcategories of a given category
	- Limited to 500 results

	PARAMETERS:
	- category: String representing category to search under
		(with "Category:" removed)

	RETURN: List of strings representing subcategories
		(with "Category:" removed)
	"""
	params = {
		"action": "query",
		"cmtitle": "Category:" + category,
		"cmtype": "subcat",
		"list": "categorymembers",
		"format": "json",
		"cmlimit": 500,
	}
	response = S.get(url=url, params=params)
	data = response.json()
	subcats = []
	for item in data["query"]["categorymembers"]:
		subcats.append(item["title"].replace("Category:", ""))
	return subcats

print(getSubCategories("Business"))

