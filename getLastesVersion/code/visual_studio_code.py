#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests as req
def getVersion() : 
    resp = req.get("https://code.visualstudio.com/updates/")
    return resp.url.split('/')[-1]

def getName() : 
    return "Visual Studio Code"

if __name__ == '__main__' : 
    print(getVersion())