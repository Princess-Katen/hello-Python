#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:11:23 2020

@author: tatyanamironova
"""
'''
times = input('How many times do I have to tell you? ')
times = int(times)

for i in range(times):
    print('Clean up your room')
    if i >= 4:
        print('Do you even listen?')
        break
'''

from random import randint  # use randint(a, b) to generate a random number between a and b

number = 0 # store random number in here, each time through
i = 0  # i should be incremented by one each iteration
while number != 5 :
    i += 1
    number = randint(1,10)
    print(number)
