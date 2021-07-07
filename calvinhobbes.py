#Calvin and hobbes comic strip downloader

#imports
import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.gocomics.com/random/calvinandhobbes')
print(page.url)