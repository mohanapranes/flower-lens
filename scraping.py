from bs4 import BeautifulSoup as bs
import requests
import wikipedia
def scraping(name):
    result = wikipedia.summary(name, sentences = 3)

    html_text = requests.get('https://en.wikipedia.org/wiki/'+name).text
    soup = bs(html_text,'lxml')
    name = soup.find('h1',class_='firstHeading').text

    details = soup.find('table', class_='infobox biota')
    list = [[]]
    list.append(["Botanical name:",name])
    for tr in details.find_all('tr'):
        tds = tr.find_all('td')
        if(len(tds)==1):
            temp=[]
            temp.append(tds[0].text)
            list.append(temp)
        elif(len(tds)>1):
            temp=[]
            temp.append(tds[0].text)
            temp.append(tds[1].text)
            list.append(temp)
    list.append(["summary:",result])
    return list
