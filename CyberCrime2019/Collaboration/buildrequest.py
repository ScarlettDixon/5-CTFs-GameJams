#!/usr/bin/python

import hashlib

cookie_f = open("cookie.txt", "r")
index = int(cookie_f.readline())
cookie = cookie_f.readline()
print("cookie: " +cookie)
cookie_f.close()

request_f = open("./requests/request-" + str(index) + ".txt", "r")
request = request_f.read()
request_f.close()

result = hashlib.sha1(str.encode(str(index)))
modifiedRequest = request.replace("DNT: 1", "Cookie: PHPSESSID=" + cookie + "\nDNT: 1")

new_request_f = open("newrequest.txt", "w")
new_request_f.write(modifiedRequest)
new_request_f.close()	


		
		