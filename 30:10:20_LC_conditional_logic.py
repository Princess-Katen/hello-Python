#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 17:01:29 2020

@author: tatyanamironova
"""
"""
numbers = [1, 2, 3, 4, 5, 6]
print([num for num in numbers if num % 2 == 0]) #even
print([num for num in numbers if num % 2 != 0]) #odds
"""
"""
numbers = [1, 2, 3, 4, 5, 6]
print([num*2 if num % 2 == 0 else num/2 for num in numbers])
"""
"""

#print only consonants + joining something into the string

with_vowels = "This is so much fun!"

print([char for char in with_vowels if char not in "aeiou"])
print(''.join(char for char in with_vowels if char not in "aeiou"))
"""
print('...'.join(["Puck", "Chiki", "Bug"]))
