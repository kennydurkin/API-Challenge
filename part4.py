#Author: Kenny Durkin
#Fourth stage of CODE2040 API Challenge

import requests,json,datetime,dateutil.parser,api
from auth import settings

#register with the API
email = settings['email']
github = settings['github']
token = api.getToken(email,github)
print 'Token is ' + token

#receive the dict
url = 'http://challenge.code2040.org/api/time'
info={'token':token}
resp = api.postData(url,info)
datestamp = resp['datestamp']
interval = resp['interval']

print datestamp

datestamp = dateutil.parser.parse(datestamp)
future = datestamp + datetime.timedelta(0,interval)
iso_future = future.isoformat()

print datestamp
print future
print iso_future

#send the time
url = 'http://challenge.code2040.org/api/validatetime'
info={'token':token,'datestamp':iso_future}
print api.postData(url,info)
