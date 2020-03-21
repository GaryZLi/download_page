from bs4 import BeautifulSoup
import requests
import urllib.robotparser

def getURL(site):
    tld = {'com', 'net'}
    site = site.lower()
    url = ''

    for i in range(0, len(site)):
        if site[i] == '.':
            if site[i+1:i+4] in tld:
                return site[0:i+4]
    
    return url

def scrape(website, file):
    req = requests.get(website)
    
    bs = BeautifulSoup(req.content, 'lxml').prettify()

    with open('results.html', 'w') as file:
        for char in bs:
            try:
                file.write(char)
            except:
                pass