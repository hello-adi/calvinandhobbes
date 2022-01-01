# calvinandhobbes - comic downloader
A script to scrape and download calvin and hobbes comic strips using BeautifulSoup4

 
## Introduction
The project uses BeautifulSoup4 to scrape the website gocomics.com for calvin and hobbes comics. The comic strip is then downloaded to the PC using Wget.
	
## Requirements
Project uses:
* Python version: 3.8.10
* Requests version: 2.22.0
* BeautifulSoup4 version: 4.8.2
* Wget version: 3.2
	
## Installing on local machine
The application uses BeautifulSoup, Requests and Wget which are not availible in the standard python library, therefore they must be downloaded using [pip](https://pip.pypa.io/en/stable/). 

``` bash
pip install beautifulsoup4
pip install requests
pip install wget
```

## Using calvinandhobbes
The application does not require any special inputs. Simply running it will download a comic strip into the file directory. 

## Credits
The project was inspired by myNameArnav's [xkcd downloader](https://github.com/myNameArnav/xkcdDownloader)

## Future scope
The overall idea is automating running the script everyday so the user has a comic strip waiting for them at a specific time e.g., in the morning. This can be achieved either by simply running the script everyday at a predefined time or utilising a library which sends the downloaded comic strip to the user by e-mail everyday.
