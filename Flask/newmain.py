import requests
import bs4


def web_scrape(query):
    # text = "geeksforgeeks"
    url = 'https://google.com/search?q=' + query
    request_result = requests.get(url)
    soup = bs4.BeautifulSoup(request_result.text, "html.parser")
    heading_object = soup.find_all('a')
    TAGS = list()
    for info in heading_object:
        href = info["href"]
        if href.startswith('/url?q='):
            TAGS.append(href.lstrip('/url?q='))
    return TAGS
# web_scrape()
