#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 16:17:42 2020

@author: tatyanamironova
"""
age = 21
# 2-6 2 dollar ticket
# over 65 5 dollar ticket
# 10 dolar for all the other
if not ((age >= 2 and age <= 6) or age >= 65):
    print('you pay 10 dollars and you are not a child or a senior')
else:
    print('you are a child or a senior')
