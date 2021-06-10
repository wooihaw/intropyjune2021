# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 09:06:56 2021

@author: wooihaw
"""
#%% Day-2 Recap
astring1 = 'This is a string'
astring2 = "This is also a string"
astring3 = "Let's start Pythong programming"

alist = [1, 2.3, 4+5j, 'abc', [67.8, -9.1], {'apple':1.2, 'orange':2.5}]
atuple = (1, 2.3, 4+5j, 'abc')
adict = {'name': 'John', 'phone': 12345678}
aset = {1, 2.3, 'abc'}

print(f'{astring1.upper()=}')

alist.append([23.4, -56.7])
print(f'{alist=}')

adict['addr'] ='123, First Avenue'
print(f'{adict=}')
print(f"{adict.get('name', 'unknown')=}")

#%% Open file for writing
with open('test.txt', 'w') as outfile:
    outfile.write('This is a test file.\n')
    
#%% Open file for reading
with open('test.txt', 'r') as infile:
    s = infile.read()
print(s)

#%% Open file for appending
with open('test.txt', 'a') as outfile:
    outfile.write('We are appending to the file.')
    