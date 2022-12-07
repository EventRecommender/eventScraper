import requests
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser

import importlib.util
import os
import sys
fileNoExistenceReponse = True
parser = RobotFileParser()

def moduleAvailable(url):
    """Checks if a Url is available for Crawling"""
    parser.set_url(url)
    parser.read()
    if requests.head(url + "/robots.txt").status_code == 200: return parser.can_fetch("*", url)
    else: 
        if requests.head(url).status_code == 200: return fileNoExistenceReponse
        else: return False


def ImportModules():
    """Imports all modules from /Souces folder. Returns modules available for scraping"""
    importedModules = []
    #Retrives all .py files from Sources
    modules = [file for file in os.listdir('./Sources') if file.endswith('.py')]
    
    for module in modules:
        name = module.split('.')[0]
        mod = importlib.util.spec_from_file_location(name, './Sources/'+ module).loader.load_module()
        if moduleAvailable(mod.getUrl()): importedModules.append(mod)
        
    return importedModules

def CollectContent(modules):
    """Retrives events for each module in a list."""
    collectedEvents = []
    for module in availableModules: 
            events = module.getContent()
            if len(events) > 0: collectedEvents.append(events)
        
    
    return collectedEvents

def PrettyPrint(eventlists, PrintEvents: bool):

    for eventlist in eventlists:
        print(eventlist[0]['host'] + ': [' + str(len(eventlist)) +']')

        if PrintEvents == True:
            for event in eventlist:
                print('-----------------------------------------')
                print('Title: ' + str(event['title']))
                print('Date: ' + str(event['date']))
                print('Type: ' + str(event['type']))
                print('Place: ' + str(event['place']))
                print('Host: ' + str(event['host']))
                print('URL: ' + str(event['url']))
                print('-----------------------------------------')
            print('#########################################')

def Start():
    availableModules = ImportModules()
    eventLists = CollectContent(availableModules)
    # if len(sys.argv) > 1 and str(sys.argv[1]).lower() == 'test': PrettyPrint(eventLists, False)
    # else: PrettyPrint(eventLists, True)
    return eventLists
    

    

    
    