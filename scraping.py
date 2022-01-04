from bs4 import BeautifulSoup as bs
import requests

html_text = requests.get('https://en.wikipedia.org/wiki/Adenium').text
soup = bs(html_text,'lxml')
name = soup.find('h1',class_='firstHeading').text
print("Botanical name:",name)

details = soup.find('table', class_='infobox biota')
list = [[]]
for tr in details.find_all('tr'):
    tds = tr.find_all('td')
    if(len(tds)>1):
        temp=[]
        temp.append(tds[0].text)
        temp.append(tds[1].text)
        list.append(temp)
for i in list:
    print(i)

