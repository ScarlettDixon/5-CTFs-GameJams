#!/usr/bin/python
"""
10.10.241.214
10.10.112.87
"""
import requests as req


"""
path = 'robots.txt'
host = 'https://tryhackme.com/'
while(host != ''):
    response = req.get(host + path)
    print(response)
    status_code = response.status_code
    print(status_code)
    text = response.text
    print(text)
    host=''
"""   
    
#path = 'index.html'
host = 'http://10.10.112.87'
host = 'http://10.10.241.214'
path = '/'
check = 'start'
values=''
nxt = ''
while(check != 'end'):
    response = req.get(host + ':3000' + path + nxt)
    print(response)
    status_code = response.status_code
    print(status_code)
    text = response.text
    print(text)
    json = response.json()
    #jsone = json
    #print(jsone)
    val = json["value"]
    values += val
    nxt = json["next"]
    check = val
    
print(values)