# Python program to write JSON
# to a file


import json
import requests

# Data to be written
dictionary ={
	"name" : "sathiyajith",
	"rollno" : 56,
	"cgpa" : 8.6,
	"phonenumber" : "9976770500"
}

with open("sample.json", "w") as outfile:
	json.dump(dictionary, outfile)
print(dictionary)
url='http://admin:password-1@34.71.52.107:3000/:3000/api/dashboards/db'
data='''{
  "dashboard": {
    "id": null,
    "uid": "mahadev",
    "title": "scriptedDashboard",
    "tags": [ "templated" ],
    "timezone": "browser",
    "schemaVersion": 16,
    "version": 0
  },
  "folderId": 48,
  "overwrite": false
}'''
headers={"Content-Type": 'application/json'}
response = requests.post(url, data=data,headers=headers)
print (response.text)
