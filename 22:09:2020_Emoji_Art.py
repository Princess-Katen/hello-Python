#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 12:01:59 2020

@author: tatyanamironova
"""
x = "\U0001f600"
for y in range(3):
    #print('Starting main loop number ', y)
    for num in range(0,10):
        #print('Starting nested loop number ', num)
        print(x*num)
        num += 1
    
    
'''
x = "\U0001f600"
num = 1
while num < 11:
    print(x*num)
    num += 1
'''