from googleapiclient.discovery import build
import flask as Flask
import json
import requests


#testing the response

response = requests.get("http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json")
print(response)
#print(response.json())

#iterating through the list

for data in response.json():
    print(data['title'])
    print(data['link'])
print()
