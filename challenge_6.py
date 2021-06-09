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
u = set(w)
print(f'{t=}\n{s2=}\n{w=}\n{u=}')