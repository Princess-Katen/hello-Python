#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:18:18 2020

@author: tatyanamironova
"""

from random import randint
player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
    print (f'Player score: {player_wins} Computer score: {computer_wins}')
    print('Rock...')
    print('Paper...')
    print('Scissors...')
    
    player = input('(Player, make your move): ').lower()
    if player == 'quit' or player == 'q':
        break
    rand_num = randint(0,2)
    if rand_num == 0:
        computer = 'rock'
    elif rand_num == 1:
        computer = 'paper'
    else:
        computer = 'scissors'
        
    print(f'computer plays {computer}')
    
    if player == computer:
        print('Its a tie!')
    elif player == 'rock':
        if computer == 'scissors':
            print('Player wins')
            player_wins += 1
        elif computer == 'paper':
            print('computer wins')
            computer_wins += 1
    elif player == 'paper':
        if computer == 'scissors':
            print('computer wins')
            computer_wins += 1
        elif computer == 'rock':
            print('Player wins')
            player_wins += 1
    elif player == 'scissors':
        if computer == 'paper':
            print('Player wins')
            player_wins += 1
        elif computer == 'rock':
            print('computer wins')
            computer_wins += 1
    else:
        print('something went wrong')
if player_wins > computer_wins:
    print('Congrats,you won!')
elif player_wins == computer_wins:
    print('Its a tie')
else:
    print('Unfortunately, the computer won')
