# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 11:56:20 2021

@author: wooihaw
"""
#%% Variable types
var_bool = True
print(type(var_bool))

var_str = "Hello world!"
print(type(var_str))

var_int = 4
print(type(var_int))

var_float = 5.0
print(type(var_float))

var_complex = 1.0 - 3j
print(type(var_complex))

var_none = None
print(type(var_none))

a = var_int + var_float
print(a, type(a))

alist = [1, 2, 3, a, "five", [6, 7.89]]
print(alist, type(alist))

alist[1] = -2  # change 2nd element
print(alist)
print(len(alist))

adict = {"apple": 1.2, "banana": 2.3}
print(adict, len(adict), type(adict))
adict["banana"] = 3.4  # change the value of 'banana'
print(adict)

astring = "Introduction to Python"
print(astring, len(astring), type(astring))
print(astring[0:10])  # print the first 10 characters

#%% Operations on variables
a, b, c = 23, 45.67, 8 + 5j
print(f"{a=}, {b=}, {c=}")

c = 12.5
d = -34.78
c, d = d, c  # swap values between variables
print(f"{c=}, {d=}")

f = 28913477812398479123980459873249870923480098345 ** 3
print(f"{f=}", type(f))

print(a * b / 2.1)
print((a + b - c) * 3.1416)

str1 = " fun"
# print(3 + str1)  we cannot add int to str
print(3 * str1)

str2 = "Python is"
print(str2 + str1)  # string concatenation
print(str2 + 3 * str1)

str3 = "123.456"
print(f"{str3=}", type(str3))

g = eval(str3)  # convert string to float
print(f"{g=}", type(g))

h = int(g)  # convert float to int
print(f"{h=}", type(h))

print(-(2 ** 2))  # this will give us -4
print((-2) ** 2)  # this will give us 4

#%% Input, output
ans = input('Enter a number: ')
print(f'{ans=}, {type(ans)}')

ans2 = eval(input('Enter a number: '))
print(f'{ans2=}, {type(ans2)}')

#%% while loops and conditional statement
i = 0
while i < 10:
    print(i)
    i += 1  # i = i + 1
    
while True:
    ans = input('Do you want to continue? (y/n) ')
    if ans == 'n':
        print('Bye!')
        break
    elif ans == 'y':
        print("Let's continue")

#%% for loops
a = [1, 3, 5, 'a', 'b']
for i in a:
    print(i)

b = 'hello world!'
for i in b:
    print(i)
    
for i in range(10):
    print('Hello')
    
for i in range(-10, 10, 2):
    print(i)

for i in range(3):
    print('This is in loop 1')
    for j in range(2):
        print('This is in loop 2')
    print('This is back to loop 1')
print('This is outside of the loops')

a = ['apple', 'banana', 'ciku']
b = [1.20, 2.40, 3.75, 4.8]
c = [1, 2, 3, 4, 5]

for i, j, k in zip(c, a, b):
    print(f'{i}. {j}: RM{k}')

for i, j in enumerate(a, start=1):
    print(f'{i}. {j}')

#%% Ternary if-else
ans = eval(input('Enter an integer: '))
res = 'even' if ans % 2 == 0 else 'odd'
print(f'You have entered an {res} number')

#%% Functions
def myfunc():
    pass

def make_polite(sentence):
    return sentence + ', please'

print(make_polite('Pass me the cheese'))
print(make_polite('Order me a pizza'))

#%% Modules
import math
print(math.cos(math.pi))

import math as m
print(m.sin(m.pi/2))

from math import sin, cos, pi
print(sin(pi/2), cos(pi))

#%% Strings
str1 = '''This is a multiple lines \
string that is spanning multiple lines \
of text.'''
print(str1)

print('Let\'s try out Python programming')
print('This is Line 1\\nThis is still Line 1')

print('This is a new line character \\n.')
print(r'This is a new line character \n.')

s = 'This is a simple string.'
print(s[0])  # First character
print(s[-1])  # Last character
print(s[:4])  # first 4 characters
print(s[-7:]) # last 7 characters
print(s[0:12:2])  # start from first character and skip one character each time
print(s[::-1])  # reverse the string

quantity = int(input('Enter quantity: '))
price = float(input('Enter the price: '))
print(f'Total price for {quantity} apples is RM{quantity*price:.2f}')

#%% Unicodes
emoji = '????'
print(f'Today is a {emoji} day')

print(ord(emoji))  # show the unicode for the emoji

for i in range(50):
    print(ord(emoji)+i, chr(ord(emoji)+i), sep=': ', end=' ')

#%% String methods
str1 = 'Hello'
str2 = 'world'
str3 = '123'
str4 = 'Testing123'

print(f'{str1=} consists of alphabets only: {str1.isalpha()}')
print(f'{str3=} consists of alphabets only: {str3.isalpha()}')
print(f'{str3=} consists of digits only: {str3.isdigit()}')
print(f'{str4=} consists of alphabets & digits only: {str4.isalnum()}')
print(f'{str1.lower()} {str2.upper()}')
print(f'{str4.swapcase()}')

str5 ='to be or not to be'
print(str5.count('o'))
print(str5.replace('to', 'no', 1))  # only replace the first 'to'
alist = str5.split()
print(alist)

str6 = '1'
print(str6.zfill(5))

blist = list(str1)
print(blist)
str7 = '-'.join(blist)
print(f'{str7=}')