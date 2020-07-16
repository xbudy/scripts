import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
    'TE': 'Trailers',
}
def weather():
    plc1=input("where : ")##########################place
    params = (
        ('client', 'firefox-b-e'),
        ('q', 'weather'+plc1),
    )

    response = requests.get('https://www.google.com/search', headers=headers, params=params)
    html=response.text
    soup=BeautifulSoup(html, 'html.parser')
    ft=soup.find('div',{"class":"vk_bk sol-tmp"})
    weather=ft.find('span',{"id":"wob_tm"}).text
    plc=soup.find('div',{"id":"wob_loc"}).text
    tm=soup.find('div',{"id":"wob_dts"}).text
    hz=soup.find('span',{"class":"vk_gy vk_sh"}).text
    print("its : ",weather," at : ",tm," in : ",plc,"mean its : ",hz )
try :
    
    while True:
        weather()
except:
    print("choose valid place")
    while True:
        weather()
