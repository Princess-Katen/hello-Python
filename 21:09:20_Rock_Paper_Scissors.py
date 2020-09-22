#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 12:47:47 2020

@author: tatyanamironova
"""

print('Rock...')
print('Paper...')
print('Scissors...')

Player1 = input('Player 1, make your move: ')
Player2 = input('Player 2, make your move: ')

if Player1 == 'rock' and Player2 == 'scissors':
    print('Player 1 wins')
elif Player1 == 'rock' and Player2 == 'paper':
    print('Player 2 wins')
elif Player1 == 'paper' and Player2 == 'scissors':
    print('Player 2 wins')
elif Player1 == 'paper' and Player2 == 'rock':
    print('Player 1 wins')
elif Player1 == 'scissors' and Player2 == 'paper':
    print('Player 1 wins')
elif Player1 == 'scissors' and Player2 == 'rock':
    print('Player 2 wins')
elif Player1 == Player2:
    print('Its a tie!')
else:
    print('something went wrong')
    