from time import sleep
from bs4 import BeautifulSoup
import requests

def getUrl():
    return 'https://akkc.dk/musik-teater/kalender/'

def getContent(): 
    eventList = []
    html = getHtml(getUrl())
    events = html.find_all('div', {'class': 'border-wrap'})
    events.pop(0) #removes the element only containg (menu text)
    for event in events:
            currentEvent = {
                'img': 'https://akkc.dk'+ event.find('img')['src'],
                'title': event.find('span', {'class': 'name'}).get_text(),
                'place': "aalborg",
                'host':  'AKKC',
                'date': CreateDate(event.find('span', {'class': 'date-and-time'}).get_text()),
                'type': event.find('span',{'class': 'genre'}).get_text(),
                'url': 'https://akkc.dk' + event.find('a', {'class': 'full-link'})['href']
            }          
            eventList.append(currentEvent)
    
    return eventList

def CreateDay(day):
    return day.replace('.','')

def CreateDate(date):
    splitDate = date.split(' ')
    return splitDate[3] +'-'+ getMonth(splitDate[2]) +'-'+ CreateDay(splitDate[1]) + ' ' + getTime(splitDate[5] + ':00')


def getMonth(str):
    month = str.lower()
    match month:
        case 'januar': return '01'
        case 'februar': return '02'
        case 'marts': return '03'
        case 'april': return '04'
        case 'maj': return '05'
        case 'juni': return '06'
        case 'juli': return '07'
        case 'august': return '08'
        case 'september': return '09'
        case 'oktober': return '10'
        case 'november': return '11'
        case 'december': return '12'
    
def getTime(str):
    return str.replace('.', ':')

   
def getHtml(url):
    return BeautifulSoup(requests.get(url).text, 'html.parser')

