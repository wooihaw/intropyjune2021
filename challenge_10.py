# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 16:11:19 2021

@author: wooihaw
"""
# Challenge 10
temperatures = []
with open('data/Heathrow.txt') as f:
    for row in f:
        temperatures.append(float(f.readline().strip()))

print(temperatures)