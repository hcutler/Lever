import json
import urllib
import requests
import urllib2


url = 'https://api.lever.co/v0/postings/leverdemo?mode=json'
data = '{"query":{"id":[{}]}'

response = requests.get(url, data=data)
if (response.ok):
  jData = json.loads(response.content)
  for key in jData:
    print jData[0]
else:
  print response.raise_for_status()