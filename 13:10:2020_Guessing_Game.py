#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 13:58:52 2020

@author: tatyanamironova
"""

import random

random_number = random.randint(1,10)
guess = None

while guess != random_number:
    guess = input('print the number from 1 to 10: ')
    guess = int(guess)      
    if guess < random_number:
        print('Too low, try again')
    elif guess > random_number:
        print('Too high!')
    else:
        print('You won!')
print(random_number)
