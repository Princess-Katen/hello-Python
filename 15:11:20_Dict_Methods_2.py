#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 12:56:15 2020

@author: tatyanamironova
"""
##pop
#user_info = {"who": "Katten", "what": "loves", "whom": "Medvezhaten"}
#user_info.pop("who")

##popitem
# user_info = {"who": "Katten", "what": "loves", "whom": "Medvezhaten"}
# user_info.popitem()

##update
user_info = {"who": "Katten", "what": "loves", "whom": "Medvezhaten"}
person = {"city": "Bogoroditsk"}
person.update(user_info)
print(person)