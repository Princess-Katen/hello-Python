#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:02:42 2020

@author: tatyanamironova
"""

x = 3
ans = 0
itersLeft = x
while itersLeft != 0:
    ans = ans + x
    itersLeft = itersLeft - 1
print(str(x) + "*" + str(x) + "=" + str(ans))