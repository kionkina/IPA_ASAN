'''
Karina Ionkina
SoftDev1 pd07
K#13: A RESTful Journey Skyward
2017-11-09
'''

import urllib2
import json
from flask import Flask, render_template

api_key= "4Gh1MmyY5cA9nGRSD9sf5RLAHZAJNQLrGr1suKnz"

uResp = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key="+ api_key)
temp = uResp.read()
data = json.loads(temp)

#print data

img_url= data['hdurl']
print img_url

exp= data['explanation']
print exp


app = Flask(__name__)

@app.route('/')
def foo():
    return render_template('home.html', img_url = img_url, exp = exp)

if __name__ == "__main__":
    app.debug = True
    app.run()



"""
----------- playin with planetary sounds API ----------------------------------------
uResp = urllib2.urlopen("https://api.nasa.gov/planetary/sounds?q=apollo&api_key=" + api_key)

uResp = uResp.read()
#print uResp

d = json.loads(uResp)

#print d["results"]

for dictionary in d["results"]:
    for key in dictionary:
        print str(key) + " ------ " + str(dictionary[key])
    print "-----------------------------------------------------------------------------------"
"""



