import requests

from bs4 import BeautifulSoup
URL = 'http://books.toscrape.com/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())