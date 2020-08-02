import requests
from bs4 import BeautifulSoup
import time
import re
import os
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://shahiid-anime.net/episodes/?season=12768',
    'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
}
numbreofserie='12768'
key='https://shahiid-anime.net/episodes/kono'
url='https://shahiid-anime.net/episodes/?season='+numbreofserie
allerrors=[]
def get_mp4upload(url, keyw, p):
  links=[]
  if p=='d':
      response = requests.get(url, headers=headers)
      page=response.text
      soup=BeautifulSoup(page, 'html.parser')
      firsturlss=soup.find('div', class_="alignright")
      g=firsturlss.find('a')
      try:
        ljk=(len(g))
      except:
        g=False
        return g

  if p=='A':
      response = requests.get(url, headers=headers)
      page=response.text
      soup=BeautifulSoup(page, 'html.parser')
      firsturlss=soup.find_all('a')
      #print(list(yrls.children))
      for i in firsturlss:
        if keyw in str(i):
          l=i.get('href')
          return l   
          #############""
  response = requests.get(url, headers=headers)
  page=response.text
  soup=BeautifulSoup(page, 'html.parser')
  allliks=soup.find_all('a')
  #print(list(yrls.children))
  #print(allliks)
  for i in allliks:
    if keyw in str(i):
      l=i.get('href')
      links.append(l)
  return links
linksofeps=[]

l=0
for i in range(0, 10):
  urla='https://shahiid-anime.net/episodes/page/'+str(i)+'/?season='+numbreofserie
  if get_mp4upload(urla,'https://shahiid-anime.net/episodes/page','d')==False:
    break
  l+=1

def appendtoeps(listy):
  for i in listy:
    linksofeps.append(i)
appendtoeps(get_mp4upload(url,key,''))
for i in range(2,l+1):
  urlb='https://shahiid-anime.net/episodes/page/'+str(i)+'/?season='+numbreofserie
  appendtoeps(get_mp4upload(urlb, key,''))
linksofeps=list(dict.fromkeys(linksofeps))
#for i in linksofeps:
##  print(i)
#  print("")
#  time.sleep(0.5)
#print(linksofeps)
list_of_mp4upload=[]
listes={}
for link in linksofeps:
  respons=requests.get(link, headers=headers)
  page=respons.text
  soup=BeautifulSoup(page, 'html.parser')
  class_oflinks=soup.find_all('a', class_='buttosn')
  if 'Mp4upload' not in str(class_oflinks):
    errorr='no mp4 for : '+link
    allerrors.append(errorr)
  for i in class_oflinks:
    if 'Mp4upload' in str(i):
      list_of_mp4upload.append(i.get('data-frameserver'))
      l=i.get('data-frameserver')
      listes[link]=l
for i in list_of_mp4upload:
  if '.html' not in str(i):
    list_of_mp4upload.remove(i)

full=[]
liop=[]
for i in listes:
  url='https://www.mp4upload.com/embed-'+listes[i]
  ress=requests.get(url, headers=headers)
  page=ress.text
  soup=BeautifulSoup(page, 'html.parser')
  find_sc=soup.find_all('script', {"type":"text/javascript"})
  try:
    stroffind=str(find_sc[-1])
  except:
    error1=' haaaa 7salti ', listes[i]
    allerrors.append(error1)
  flag=re.sub(r'[^\w]', ' ', stroffind).split()
  the_part_oflink=flag[208]
  if the_part_oflink=='282':
    the_part_oflink=flag[207]
  serv=flag[180]
  if serv=='allowfullscreen':
    serv=flag[179]
  orl='https://'+serv+'.mp4upload.com:282/d/'+the_part_oflink+'/video.mp4'
  liop.append(orl)
'''
for i in list_of_mp4upload:
  url='https://www.mp4upload.com/embed-'+i
  ress=requests.get(url, headers=headers)
  page=ress.text
  soup=BeautifulSoup(page, 'html.parser')
  find_sc=soup.find_all('script', {"type":"text/javascript"})
  try:
    stroffind=str(find_sc[-1])
  except:
    print(i,' haaaa 7salti ')
  flag=re.sub(r'[^\w]', ' ', stroffind).split()
  the_part_oflink=flag[208]
  if the_part_oflink=='282':
    the_part_oflink=flag[207]
  serv=flag[180]
  if serv=='allowfullscreen':
    serv=flag[179]
  orl='https://'+serv+'.mp4upload.com:282/d/'+the_part_oflink+'/video.mp4'
  full.append(orl)
'''
for i in liop :
  #os.system('wget --no-check-certificate '+i)
  print(i)
print(allerrors)
#print(error)


  

#print(list_of_mp4upload)
