from bs4 import BeautifulSoup as bs
import requests
import wikipedia
import json

def scraping(name):
    result = wikipedia.summary(name, sentences = 3)

    html_text = requests.get('https://en.wikipedia.org/wiki/'+name).text
    soup = bs(html_text,'lxml')
    name = soup.find('h1',class_='firstHeading').text

    details = soup.find('table', class_='infobox biota')
    list = []
    list.append({"Botanical name:":name})
    try:
        for tr in details.find_all('tr'):
            tds = tr.find_all('td')
            if(len(tds)==1):
                temp=[]
                temp.append(tds[0].text[:-2])
                list.append(temp)
            if(len(tds)>1):
                dict={tds[0].text[:-2]:tds[1].text[:-2]}
                list.append(dict)
    except:
        print('error')
    list.append({"summary:":result})
    #print(list)
    json_list = json.dumps(list)
    return json_list
