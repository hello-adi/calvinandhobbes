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
#image-url
# <a itemprop="image" class="js-item-comic-link item-comic-link-disabled" title="Calvin and Hobbes">

#   <picture class="item-comic-image"></picture>
# <img class="img-fluid lazyloaded" srcset="https://assets.amuniversal.com/59ee0c705e0a012ee3bf00163e41dd5b 600w" data-srcset="https://assets.amuniversal.com/59ee0c705e0a012ee3bf00163e41dd5b 600w" sizes="
#                        (min-width: 992px) 600px,
#                        (min-width: 768px) 600px,
#                        (min-width: 576px) 300px,
#                        600px" alt="Calvin and Hobbes Comic Strip for August 06, 2010 " src="https://assets.amuniversal.com/59ee0c705e0a012ee3bf00163e41dd5b" width="100%"></a>
imgUrl =  soup.find('img', 'img-fluid lazyloaded')
print(imgUrl)
