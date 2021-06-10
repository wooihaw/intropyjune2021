# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 16:11:19 2021

@author: wooihaw
"""
# Challenge 10
import numpy as np

temperatures = []
with open('data/Heathrow.txt') as f:
    for row in f:
        temperatures.append(float(f.readline().strip()))

print(temperatures)

print(f'{np.min(temperatures)=}', f'{np.max(temperatures)=}',
      f'{np.mean(temperatures)=}', f'{np.median(temperatures)=}',
      sep = '\n')