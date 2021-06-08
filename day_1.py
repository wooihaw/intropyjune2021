# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 11:56:20 2021

@author: wooihaw
"""
#%% Variable types
var_bool = True
print(type(var_bool))

var_str = 'Hello world!'
print(type(var_str))

var_int = 4
print(type(var_int))

var_float = 5.
print(type(var_float))

var_complex = 1. - 3j
print(type(var_complex))

var_none = None
print(type(var_none))

a = var_int + var_float
print(a, type(a))

alist = [1, 2, 3, a, 'five', [6, 7.89]]
print(alist, type(alist))

alist[1] = -2  # change 2nd element
print(alist)
print(len(alist))

adict = {'apple':1.2, 'banana':2.3}
print(adict, len(adict), type(adict))
adict['banana'] = 3.4  # change the value of 'banana'
print(adict)

astring = 'Introduction to Python'
print(astring, len(astring), type(astring))
print(astring[0:10])  # print the first 10 characters

#%% Operations on variables
a, b, c = 23, 45.67, 8 + 5j
print(f'{a=}, {b=}, {c=}')
