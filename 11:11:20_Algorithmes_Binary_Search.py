#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 19:53:20 2020

@author: tatyanamironova
"""

def create_list(start, stop):
    result_list = []
    # print(result_list)
    for i in range(start, stop+1, 1):
        result_list.append(i)
        # print(result_list)
    # print(len(result_list))
    return result_list
   
def binary_search(puklist, item):
    low = 0
    high = len(puklist)-1
    
    mid = int((low+high)/2)
    guess = puklist[mid]
    
    steps = 0
    
    while low < high:
        mid = int((low+high)/2)
        print("mid= ", mid)
        guess = puklist[mid]
        print("guess= ", guess)
        if guess == item: #victory
            print(steps)
            return mid
        elif guess < item:
            low = mid + 1 #discarding left part of the list
        else:
            high = mid - 1
        print("high= ", high)
        print("low= ", low)
        steps += 1
    print(steps)
    return None    
        
sorted_list = create_list(0, 255)

item = 300

index = binary_search(sorted_list, item)

print(index)