#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 13:46:26 2020

@author: tatyanamironova
"""
##Define only unique cities
# cities = ["Stockholm", "Astana", "Paris", "Moscow", "Astana", "Moscow"]
# set(cities)
# # back to a list
# print(list(set(cities)))
# # printing the legth
# print(len(set(cities)))

##Methods. ADD
# cities = {"Stockholm", "Astana", "Paris", "Moscow", "Astana", "Moscow"}
# cities.add("Timbuktu")
# print(cities)

##Remove
# cities = {"Stockholm", "Astana", "Paris", "Moscow", "Astana", "Moscow"}
# cities.remove("Moscow")
# print(cities)

## To generate a set with all the UNIQUE students
group1 = {"Pablo", "Maria", "Viktor", "Michael", "Bjorn"}
group2 = {"Madelene", "Maria", "Erdogan", "Bjorn"}
print(group1 | group2)

## To generate a set with the students which are in BOTH groups
group1 = {"Pablo", "Maria", "Viktor", "Michael", "Bjorn"}
group2 = {"Madelene", "Maria", "Erdogan", "Bjorn"}
print( group1 & group2)