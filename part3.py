#Author: Kenny Durkin
#Third stage of CODE2040 API Challenge

import requests,json,api
from auth import settings

#register with the API
email = settings['email']
github = settings['github']
token = api.getToken(email,github)
print 'Token is ' + token

#receive the dict
url = 'http://challenge.code2040.org/api/prefix'
info={'token':token}
resp = api.postData(url,info)
array = resp['array']
prefix = resp['prefix']

newarray = []
for x in array:
    if not x.startswith(prefix):
        newarray.append(x)

#send the array
url = 'http://challenge.code2040.org/api/validateprefix'
info={'token':token,'array':newarray}
print api.postData(url,info)
