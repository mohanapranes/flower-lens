from bs4 import BeautifulSoup as bs
import requests

html_text = requests.get('https://en.wikipedia.org/wiki/Adenium').text
soup = bs(html_text,'lxml')
name = soup.find('h1',class_='firstHeading').text
print("Botanical name:",name)

details = soup.find('table', class_='infobox biota')
table = details.find_all('td')
print(table)
