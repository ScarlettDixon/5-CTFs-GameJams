#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string
import requests
import time
import sys
import socket
import math as ma


def sock():
    hostname = "primetime.baectf.com"
    port = 443
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((hostname, port))
    #dat = input("terminaldisc")
    #sock.send(dat.encode())
    print(sock.recv(1024))
    sock.close()

def get_primes(n):
    #m = n-1
    squar = ma.ceil(ma.sqrt(n))
    print (squar)
    for m in range(n-1, 2, -1):
        count=0
        for i in range(2, squar+1):            
            #print(m,i,m%i)
            if (m % i) == 0:
                #print(m,i)
                count+=1
        #print(m, count)    
        if (count == 0):
            return m
            
prime = get_primes(121001)
#print(prime)
sock()