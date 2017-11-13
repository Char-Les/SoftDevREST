from flask import Flask, render_template
import json
from urllib2 import Request, urlopen

'''
Charles Weng
Period 7 SoftDev
HW #13: A RESTful Journey Skyward
2017-11-09
'''
app = Flask(__name__)


@app.route("/")
def hello():
    # headers for API
    headers = {
      'Accept': 'application/json',
      'User-Agent': 'Mozilla/5.0'
    }

    page = 1
    items = []
    # loop through each page and get all the items into a list
    while(page < 10):
        # access the API
        request = Request('https://private-anon-52cd4ff0cb-bindingofisaac.apiary-proxy.com/api/v1/item?page=' + str(page), headers=headers)
        x = urlopen(request).read()
        d = json.loads(x)
        # add data and continue
        items = items + d["data"]
        page += 1
    return render_template("test.html", items=items)


if __name__ == "__main__":
    app.debug = True
    app.run()
