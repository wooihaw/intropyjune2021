# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 15:05:41 2021

@author: wooihaw
"""
# Challenge 6
s = '''Peter Piper picked a peck of pickled peppers.
A peck of pickled peppers Peter Piper picked.
If Peter Piper picked a peck of pickled peppers,
where is the peck of pickled peppers Peter Piper picked?'''

t = [c.lower() if c.isalpha() else ' ' for c in s]
s2 = ''.join(t)
w = s2.split()
u = sorted(set(w))
print(f'{t=}\n{s2=}\n{w=}\n{u=}')

wc = {}
for i in u:
    wc[i] = w.count(i)
print(f'{wc=}')

# Method 2
wc2 = {}
for i in sorted(w):
    wc2[i] = wc2.get(i, 0) + 1
print(f'{wc2=}')

# Method 3
from collections import Counter
wc3 = Counter(w)
print(f'{wc3=}')