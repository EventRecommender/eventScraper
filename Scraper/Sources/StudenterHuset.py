from time import sleep
from bs4 import BeautifulSoup
import requests

def getUrl():
    return 'https://studenterhuset.dk/'

def getContent():
    EventList = []
    html = getHtml(getUrl())

    for event in html.find_all('li', {'class': 'sm-6 md-4 eventlist__listitem'}):  
        date = event.find('span', {'class':'eventlist__date'}).get_text()
        time = event.find('span', {'class':'eventlist__meta--span eventlist__starttime'}).get_text()

        event = {
            'img': event.find('img')['src'],
            'url': 'https://studenterhuset.dk' + event.find('a')['href'],
            'title': event.find('a', {'class':'eventlist__link'}).get_text(),
            'place': "aalborg",
            'host': 'Studenter Huset',
            'date': createDate(date, time),
            'type': ""

        }
        EventList.append(event)
    
    return EventList
        

def getHtml(url):
    return BeautifulSoup(requests.get(url).text, 'html.parser')

def findAllByClass(html, type: str, classname: str):
    return html.find_all(type, {'class': classname})

def createDate(Inputdate, Inputtime):
    split = Inputdate.split('.')
    splittime = Inputtime.split(' ')
    return '20' + split[2] + '-' + split[1] + '-' + split[0] + ' ' + splittime[1] + ':00'

