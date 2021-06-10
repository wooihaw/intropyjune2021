# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 15:43:42 2021

@author: wooihaw
"""
# Challenge 7
# Using map() and filter()
alist = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, range(1, 101))))

# list comprehension
blist = [i**2 for i in range(1, 101) if i % 2 == 0]

print(f'{alist=} \n {blist=}')
