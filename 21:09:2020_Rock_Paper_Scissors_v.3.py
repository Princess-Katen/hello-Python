#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:18:18 2020

@author: tatyanamironova
"""

import random
print('Rock...')
print('Paper...')
print('Scissors...')

Player = input('Player, make your move: ').lower()

import random
rand_num = random.randint(0,2)
if rand_num == 0:
    computer = 'rock'
elif rand_num == 1:
    computer = 'paper'
else:
    computer = 'scissors'
print(f'computer plays {computer}')

if Player == computer:
    print('Its a tie!')
elif Player == 'rock':
    if computer == 'scissors':
        print('Player wins')
    elif computer == 'paper':
        print('computer wins')
elif Player == 'paper':
    if computer == 'scissors':
        print('computer wins')
    elif computer == 'rock':
        print('Player wins')
elif Player == 'scissors':
    if computer == 'paper':
        print('Player wins')
    elif computer == 'rock':
        print('computer wins')
else:
    print('something went wrong')
