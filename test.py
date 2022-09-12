from googleapiclient.discovery import build
import flask as Flask
import json
import requests


#testing the response

response = requests.get("http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json")
print(response)
#print(response.json())


# channel ids for analysis
#1 ted = UCAuUUnT6oDeKwE6v1NGQxug
#2 carwow = UCUhFaUpnq31m6TNX2VKVSVA
#3 DOUGMUNRO = UCsqjHFMB_JYTaEnf_vmTNqg
#4 Motortrend = UCsAegdhiYLEoaFGuJFVrqFQ
#5 Autocar india = UCjWs7BxyjO5SLqevxSmp4vQ
#6 faisal Khan = UCPF4bAZimS4T8w1TlbeIAYg


