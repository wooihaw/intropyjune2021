# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 16:00:59 2021

@author: wooihaw
"""
# Challenge 9
import easygui as gui
from random import choice, shuffle
animals = ['wolf', 'whale', 'cheetah', 'lizard', 'tiger', 'monkey', 'parrot',
'gorilla', 'dolphin', 'snake']

word = choice(animals)

alist = list(word)
shuffle(alist)

anagram = ''.join(alist)

guess = gui.enterbox(f'Do you know what is this animal "{anagram}"? ', title='Anagram Game')

if guess == word:
    gui.msgbox('You are genius!', title='Result')
else:
    gui.msgbox(f'Wrond answer. It should be {word}', title='Result')