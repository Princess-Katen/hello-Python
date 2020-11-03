#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 18:39:27 2020

@author: tatyanamironova
"""

# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [[print(val) for val in l] for l in nested_list]

# #nest it again
# board = [[[num for num in range(1,4)] for val in 
#           range(1,4)] for val in range(1,4)]
# print(board)

# ...and again
# board = [[[num for num in range(1,4)] for val in 
#           range(1,4)] for val in range(1,4)]
# print(board)

# #adding conditional logic
# print([["X" if num % 2 != 0 else "O" for num in range(1,4)] for 
#  val in range(1,4)])

print([["*" for x in range(1,4)] for i in range(1,4)])