from flask import Flask, render_template
import json
import urllib2

'''
Charles Weng
Period 7 SoftDev
K #13: A RESTful Journey Skyward
2017-11-09

I"m not sure why it's sayintg load takes only one arguement when I'm using loads, but I'm pretty sure this works
'''
app = Flask(__name__)


@app.route("/")
def load(arg):
    uResp = urllib2.openurl('https://api.nasa.gov/planetary/apod?api_key=bBTrtmlfj4piBfET10iuLi3tsaHJMaKJiLGcguU3')
    d = json.loads(uResp.read())
    print d
    return render_template("test.html", url=d[url], exp=d[explanation], date=d[date])


if __name__ == "__main__":
    app.debug = True
    app.run()
