# Calvin and hobbes comic strip downloader

# imports
import requests
from bs4 import BeautifulSoup
import wget

# page url

page = requests.get('https://www.gocomics.com/random/calvinandhobbes')

# BeautifulSoup object with lxml parser
soup = BeautifulSoup(page.content, 'lxml')

# extracting image url class_=img-fluid lazyloaded
img = soup.find('picture', 'item-comic-image')

# getting image source by finding element by id
imgSource = img.find("img")

# get image url by using src tag
imgURL = imgSource['src']

# downloading image to pc using wget.
wget.download(imgURL)
