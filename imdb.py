import requests
from bs4 import BeautifulSoup
import random
import webbrowser

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
}

response = requests.get('https://www.imdb.com/chart/top', headers=headers)
soup=BeautifulSoup(response.text, 'html.parser')
tbody=soup.find_all('td',class_='titleColumn')
######
######
while True:

    nmb=random.randint(0,250)
    name=tbody[nmb].find('a').text
    #######################""
    year=tbody[nmb].find('span').text
    ######################""
    link='https://www.imdb.com'+tbody[nmb].find('a').get('href')
    reso=requests.get(link,headers=headers)
    soup=BeautifulSoup(reso.text, 'html.parser')
    trailer=soup.find('a',class_='slate_button prevent-ad-overlay video-modal').get('href')
    trailerLINK='https://www.imdb.com'+trailer
    print('how about: '+name+'  '+year)
    print('trailer link: '+trailerLINK)
    wht=input('go to trailer hit "a" new one hit "enter" exit(any key)')
    if wht=='a' or wht=='A':
        webbrowser.open(trailerLINK)
    if wht == '':
        continue
    else:
        break
