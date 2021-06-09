# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 14:15:26 2021

@author: wooihaw
"""
# Challenge 1
heads = 35
legs = 94

for r in range(heads+1):
    c = heads - r
    if (2*c + 4*r) == legs:
        print(f'We have {r} rabbits and {c} chicken')