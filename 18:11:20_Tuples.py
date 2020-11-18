#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 13:04:10 2020

@author: tatyanamironova
"""
##intro
# alphabet = ('a', 'b', 'c', 'd')
# type(alphabet)
# # alphabet.append('e')
# alphabet[0] = 'A'

##Months
# Months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 
#           'August', 'September', 'October', 'November', 'December')
# Months[7]

##Tuples as keys
# locations = {
#     (24.444, 54.765): 'Tokyo office',
#     (76.324, 97.657): 'Stockholm office',
#     (34.867, 86.765): 'Minsk office' 
#     }
# print(locations[(34.867, 86.765)])

# ##Looping
# names = ('Katen', 'Princess', 'Meow', 'Bjorn')
# for name in names:
#     print(name)

##Printing backwards
Months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 
           'August', 'September', 'October', 'November', 'December')
i = len(Months) - 1
while i>= 0:
    print(Months[i])
    i -= 1
    
    
    
    
    
    
    