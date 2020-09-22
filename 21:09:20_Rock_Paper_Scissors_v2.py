#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:05:06 2020

@author: tatyanamironova
"""

print('Rock...')
print('Paper...')
print('Scissors...')

Player1 = input('Player 1, make your move: ')
print('*****NO CHEATING****\n' * 30)
Player2 = input('Player 2, make your move: ')
if Player1 == Player2:
    print('Its a tie!')
elif Player1 == 'rock':
    if Player2 == 'scissors':
        print('Player 1 wins')
    elif Player2 == 'paper':
        print('Player 2 wins')
elif Player1 == 'paper':
    if Player2 == 'scissors':
        print('Player 2 wins')
    elif Player2 == 'rock':
        print('Player 1 wins')
elif Player1 == 'scissors':
    if Player2 == 'paper':
        print('Player 1 wins')
    elif Player2 == 'rock':
        print('Player 2 wins')
else:
    print('something went wrong')