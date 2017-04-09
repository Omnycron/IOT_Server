#!/usr/bin/python
import Adafruit_DHT
import urllib
import json
import urllib2
import time
import requests

url = "http://192.168.0.31:5000/weather/api/readings/"
sensor2 = Adafruit_DHT.DHT22
pin = 4

while True:
    humidity, temp2 = Adafruit_DHT.read_retry(sensor2, pin)

    tempavg = temp2

    data = {
        "temp1" : 0,
        "temp2" : temp2,
        "tempavg" : tempavg,
        "pressure" : 0,
        "sealevelpressure": 0,
        "humidity": humidity,
    }

    headers = {
        "Connection" : "keep-alive",
        "Content-Type": "application/json; charset=UTF-8",
    }
    
    print "sending request"
    requests.post(url, json=data, headers=headers)
    time.sleep(60)
#req = urllib2.Request(url, urldata, headers)
#response = urllib2.urlopen(req)
#the_page = response.read()

