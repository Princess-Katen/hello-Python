#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 16:42:38 2020

@author: tatyanamironova
"""
print('How many km have you run today?')
kms = input()
miles = float(kms)/1.666
print(f'your {kms} kms ride is equal to {round(miles,2)} miles')