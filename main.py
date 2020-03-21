from functions import *

while True:
    link = input('Copy link here: ')
    
    try:
        print('scraping')
        scrape(link, 'results.html')
        print('done')
        break
    except:
        print("link invalid\n")