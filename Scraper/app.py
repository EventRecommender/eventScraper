from flask import Flask

import functions

app = Flask(__name__)

@app.get("/Scrape")
def Scrape():
    eventList = functions.Start()
    return eventList

if __name__ == "__main__":
    print("Hello")
    app.run(debug=False)