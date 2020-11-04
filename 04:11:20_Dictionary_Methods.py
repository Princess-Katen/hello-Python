#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:36:14 2020

@author: tatyanamironova
"""
##.copy
# user_info = {"who": "Katten", "what": "loves", "whom": "Medvezhaten"}
# d = user_info
# c = d.copy()
# print(c)

##.fromkeys
# new_user = {}.fromkeys(["name", "score", "email", "profile bio"], "unknown")
# new_user = {}.fromkeys('Katen', 'unknown')
# new_user = {}.fromkeys(range(1,10), 'unknown')

##get
user_info = {"who": "Katten", "what": "loves", "whom": "Medvezhaten"}
user_info.get("who")
