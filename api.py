#Author: Kenny Durkin
#Helper methods to simplify querying the API

import json,requests

def getToken(email,github):
    url = 'http://challenge.code2040.org/api/register'
    data = {'email':email,'github':github}
    resp = requests.post(url,data=json.dumps(data))
    return resp.json()['result']

def postData(url,data):
    resp = requests.post(url,data=json.dumps(data))
    return resp.json()['result']
