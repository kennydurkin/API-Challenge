#Author: Kenny Durkin
#Second stage of CODE2040 API Challenge

import requests,json,api
from auth import settings

#register with the API
email = settings['email']
github = settings['github']
token = api.getToken(email,github)
print 'Token is ' + token

#receive the dict
url = 'http://challenge.code2040.org/api/haystack'
info={'token':token}
resp = api.postData(url,info)
haystack = resp['haystack']
needle = resp['needle']

#find the needle
index = 0
for x in haystack:
    if x == needle:
        needle = index
        break
    index += 1

#send the index
url = 'http://challenge.code2040.org/api/validateneedle'
info={'token':token,'needle':needle}
print api.postData(url,info)
