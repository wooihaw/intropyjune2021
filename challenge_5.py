# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 14:55:20 2021

@author: wooihaw
"""
# Challenge 5
d = {}
for i in range(3):
    name = input(f'Enter name {i+1}: ')
    age = input(f'Enter age {i+1}: ')
    d[name] = age  # store name & age in dictionary as key-value pair

n = input('Enter a name to search: ')
print(f'{n}\'s age is {d.get(n, "unknown")}')