# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 14:37:06 2021

@author: wooihaw
"""
# Challenge 3
alist = ['Python', 'Java', 'Perl', 'PHP', 'JavaScript', 'C++', 'C#', 'Ruby', 'R']

# Method 1 - Using for loop
blist = []
for i in alist:
    if i[0].upper()=='P':
        blist.append(i)
print(f'{blist=}')
