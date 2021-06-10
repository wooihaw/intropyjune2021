# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 16:21:35 2021

@author: wooihaw
"""
# Challenge 11

from collections import Counter

with open('data/alice.txt', 'r') as f:
    s = f.read()

t = [c.lower() if c.isalpha() else ' ' for c in s]
w = (''.join(t)).split()

wc = Counter(w)
print(f'Number of unique words: {len(wc)}')