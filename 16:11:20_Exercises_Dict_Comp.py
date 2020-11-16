#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 13:30:04 2020

@author: tatyanamironova
"""

# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]
 
# answer = {list1[i]: list2[i] for i in range(0,3)}
# print(answer)

## create a dictionary fron pairs of lists
##variant 1
# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# answer = dict(person)
# print(answer)

##variant 2
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {thing[0]: thing[1] for thing in person}
print(answer)