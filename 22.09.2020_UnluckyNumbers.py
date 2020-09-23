#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:19:26 2020

@author: tatyanamironova
"""
'''
for x in range (1,21):
    if x == 4 or x == 13:
        print (f'{x} is unlucky')
    elif x % 2 != 0:
        print(f'{x} is odd')
    else:
        print(f'{x} is even')
'''
for x in range (1,21):
    if x == 4 or x == 13:
        state = 'unlucky'
    elif x % 2 != 0:
        state = 'odd'
    else:
        state = 'even'
        print(f'{x} is {state}')