from flask import Flask

import main

app = Flask(__name__)

@app.get("/Scrape")
def Scrape():
    eventList = main.Start()
    return eventList