#!/usr/bin/python

import hashlib


fd = open("request.txt", "r")
request = fd.read()

for i in range(0, 100):
	result = hashlib.sha1(str.encode(str(i)))
	#modifiedRequest = request.replace("Cookie: PHPSESSID=d46lrk1lhhr0384pqkkcsjtqqu", "Cookie: PHPSESSID=" + result.hexdigest()[:26])
	#modifiedRequest = request.replace("Cookie: PHPSESSID=d46lrk1lhhr0384pqkkcsjtqqu\n", "")
	modifiedRequest = request
	modifiedRequest = modifiedRequest.replace("formgo=1&pin=04", "formgo=1&pin=" + str(i))
	modifiedRequest = modifiedRequest.replace("Content-Length: 15", "Content-Length: "+str(13 + len(str(i))))
	out = open("request-"+str(i)+".txt", "w")
	out.write(modifiedRequest)
	out.close
fd.close()


		
		