# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 16:00:59 2021

@author: wooihaw
"""
# Challenge 9
from random import choice, shuffle
animals = ['wolf', 'whale', 'cheetah', 'lizard', 'tiger', 'monkey', 'parrot',
'gorilla', 'dolphin', 'snake']

word = choice(animals)

alist = list(word)
shuffle(alist)

anagram = ''.join(alist)

guess = input(f'Do you know what is this animal "{anagram}"? ')

if guess == word:
    print('You are genius!')
else:
    print(f'Wrond answer. It should be {word}')