#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 13:55:27 2020

@author: tatyanamironova
"""

# {num: num**2 for num in [1,2,3,4,5]}

##making every key and value uppercased
# user_info = {"who": "Katten", "what": "loves", "whom": "Medvezhaten"}
# yelling_user_info = {k.upper():v.upper() for k,v in user_info.items()}
# print(yelling_user_info)

## conditional logic
# num_list = [1,2,3,4]
# {num: ("even" if num % 2 == 0 else "odd") for num in num_list}

## making conditional logic part of the key

user_info = {"who": "Katten", "what": "loves", "whom": "Medvezhaten"}
yelling_user_info = {(k.upper() if k is "who" else k):v.upper() for k,v in user_info.items()}
print(yelling_user_info)
