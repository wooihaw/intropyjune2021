# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 09:45:26 2021

@author: wooihaw
"""
#%% Basic list examples
alist = [1, 2.3, 4+5j, 'abc', [6, 7, -8.9]]
print(alist[0])  # first item
print(alist[-1])  # last item
print(alist[-1][-1])  # this will print out -8.9
print(alist.__sizeof__())  # print the size of alist

alist[0] = -0.5
del(alist[2])  # remove item at index 2
print(alist)

alist.append('😂')  # insert at the end
print(alist)

alist.insert(2, 4-5j)  # insert 4-5j at index 2
print(alist)

alist.remove('abc')  # remove 'abc' from the list
print(alist)

blist = [34, -567.8]
clist = alist + blist  # list concatenation
print(clist)