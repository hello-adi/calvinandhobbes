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

# <picture class="item-comic-image"><img alt="Calvin and Hobbes Comic Strip for April 09, 2012 " class="lazyload img-fluid" data-srcset="https://assets.amuniversal.com/d5712420c125012fdd6d001dd8b71c47 900w" sizes="
#                        (min-width: 992px) 900px,
#                        (min-width: 768px) 600px,
#                        (min-width: 576px) 300px,
#                        900px" src="https://assets.amuniversal.com/d5712420c125012fdd6d001dd8b71c47" srcset="https://assets.gocomics.com/assets/transparent-3eb10792d1f0c7e07e7248273540f1952d9a5a2996f4b5df70ab026cd9f05517.png" width="100%"/></picture>
imgUrl =  soup.find('picture', 'item-comic-image')
print(imgUrl)
img = imgUrl.find("img")
imgThing = img['src']
print(imgThing)
