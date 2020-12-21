#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time




#try:
#    elementbtn = driver.find_element_by_class_name("btn")
#except:
#    time.sleep(timetosleep)
#    elementbtn = driver.find_element_by_class_name("btn")
#elementbtn.click()
   #Country = driver.find_element_by_id("ctl00_idPlaceHolder3_optCountry")
    #Country.click()
#AlternateCountry1 = driver.find_element_by_xpath("//select[@id='ctl00_idPlaceHolder3_optCountry']/option[value()='233']")
    #AlternateCountry1.click()
    #time.sleep(5)
#def check (i, j, k, l, m, n):
#    conc = str(i) + str(j) + str(k)+ str(l)+ str(m) + str(n)
#    print("Using:", conc)
#    elementpin = driver.find_element_by_name("pin") #.find_element_by_id("email")
#    elementpin.send_keys(conc)
#    elementpin.send_keys(Keys.RETURN)
#    time.sleep(0.25)
#    elementpin = driver.find_element_by_name("pin")
#    elementpin.send_keys(Keys.CONTROL + 'a')
#    elementpin.send_keys(Keys.DELETE)
    
def setup(wbpg):
    driver = webdriver.Firefox()
    driver.get(wbpg)
    time.sleep(0.25)
    OpenMine = driver.find_element_by_class_name("clsNavL2")
    OpenMine.click()
    time.sleep(0.25)
    Country = driver.find_element_by_xpath("/html/body/form/div[6]/div[1]/div/div[1]/select/option[233]")
    Country.click()
    Type = driver.find_element_by_xpath("/html/body/form/div[6]/div[1]/div/div[2]/select[1]/option[12]")
    Type.click()
    Display = driver.find_element_by_xpath("/html/body/form/div[6]/div[1]/div/div[3]/select[2]/option[5]")
    Display.click()
    ShowList = driver.find_elements_by_id("ctl00_idPlaceHolder3_idButtonList")
    ShowList.click()
    
if __name__ == "__main__":
    webpage = "https://www.aditnow.co.uk/"
    setup(webpage)

#/html/body/form/div[6]/div[1]/div/div[1]/select/option[232]
          