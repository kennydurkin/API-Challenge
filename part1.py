#Author: Kenny Durkin
#First stage of CODE2040 API Challenge

import requests,json,api
from auth import settings

#register with the API
email = settings['email']
github = settings['github']
token = api.getToken(email,github)
print 'Token is ' + token

#receive the string
url = 'http://challenge.code2040.org/api/getstring'
info={'token':token}

#reverse the string
string = api.postData(url,info)
print string
string=string[::-1]
print string

#send the string
url = 'http://challenge.code2040.org/api/validatestring'
info={'token':token,'string':string}
print api.postData(url,info)
