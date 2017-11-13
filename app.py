from flask import Flask, render_template
import json
import urllib2

'''
Charles Weng
Period 7 SoftDev
HW #13: A RESTful Journey Skyward
2017-11-09
'''
app = Flask(__name__)


@app.route("/")
def hello():
    uResp = urllib2.urlopen('https://api.nasa.gov/planetary/apod?api_key=bBTrtmlfj4piBfET10iuLi3tsaHJMaKJiLGcguU3')
    d = json.loads(uResp.read())
    print d
    return render_template("test.html", url=d["url"], exp=d["explanation"], date=d["date"])


if __name__ == "__main__":
    app.debug = True
    app.run()
