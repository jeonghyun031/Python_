from bs4 import BeautifulSoup
import requests
url = 'http://quotes.toscrape.com/'
html = requests.get(url)
soup = bs4(html, 'lxml')