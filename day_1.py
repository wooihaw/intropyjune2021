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
print(type(alist))