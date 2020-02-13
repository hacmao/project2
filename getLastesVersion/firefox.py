#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests as req
def getVersion() : 
    url = 'https://www.whatismybrowser.com/guides/the-latest-version/firefox'
    resp = req.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    version = soup.find_all('td')[2]
    return version.string

if __name__ == '__main__' : 
    print(getVersion())