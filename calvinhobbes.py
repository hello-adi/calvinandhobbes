#Calvin and hobbes comic strip downloader

#imports
import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.gocomics.com/random/calvinandhobbes')
print(page.url)

#BeautifulSoup object
soup = BeautifulSoup(page.content, 'lxml')
#print(soup.prettify())

#extracting image url class_=img-fluid lazyloaded
imgUrl =  soup.find('img', 'img-fluid lazyloaded')
print(imgUrl)
