#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests as req
def getVersion() : 
    url = 'https://www.whatismybrowser.com/guides/the-latest-version/chrome'
    resp = req.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    version = soup.find_all('td')[1]
    return version.string

def getName() : 
    return "Google Chrome"
if __name__ == '__main__' : 
    print(getVersion())