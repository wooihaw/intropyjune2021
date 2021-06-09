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

print(5 * blist)  # list repetition

a = []  # empty list
for i in range(5):
    a = a + [i]  # a += [i]
print(f'{a=}')

for i in range(len(a)):
    b = a.pop()  # remove last item from a and put it to b
    print(f'{b=}')
print(f'{a=}')

a = list(range(5))
print(f'{a=}')
while a:
    print(a.pop(0))  # remove first item (index 0) from a
    print(f'{a=}')

b = [21, 43, 12, -3, -7]
c = sorted(b)  # c will get a sorted copy of b in ascending order
d = sorted(b, reverse=True)  # d will get a sorted copy of b in descending order
print(f'{b=}, {c=}, {d=}')

e = b.sort()  # b itself will get be sorted, but it returns None to e
print(f'{b=}, {e=}')

b.reverse()  # b itself will be sorted (descending order)
print(f'{b=}')

print(len(b))  #  check the number of items inside list b

print(f'{alist=}')
print('😂' in alist)  # check membership of item; return True if the item is inside the list
print('abc' in alist)
print('abc' not in alist)

print(alist.index(2.3))  # get the index of 2.3 in the list

#%% Alias or copy
a = [1, 2, 3, 'a', 'b']
b = a  # b is an alias of a
c = a[:]  # c is a copy of a
print(f'{a=}, {b=}, {c=}')

print(b is a)  # check whether b is an alias of a
print(b == a)  # check whether b has the same contents as a
print(c is a)
print(c == a) 

a[2] = '😊'
a.append('x')
print(f'{a=}, {b=}, {c=}')
print(f'{id(a)=}, {id(b)=}, {id(c)=}')  # check addresses of a, b & c

#%% List comprehension
# create a list with the square of 1 to 10
a = list(range(1, 11))

# Use for loop
b = []
for i in a:
    b.append(i**2)
print(f'{a=}, {b=}')

# Use list comprehension
c = [i**2 for i in a]
print(f'{a=}, {c=}')

# create a list of even number from 0 to 50
# Use for loop
d = []
for i in range(51):
    if i % 2 == 0:
        d.append(i)
print(f'{d=}')   

e = [i for i in range(51) if i % 2 == 0]
print(f'{e=}')

#%% Write a program to calculate the number of alphabets & digits in a string
s = 'Testing 12345! Is this working correctly 67890?'

# Use for loop
c1, c2 = 0, 0
for i in s:
    if i.isalpha():
        c1 += 1  # c1 = c1 + 1
    elif i.isdigit():
        c2 += 1  # c2 = c2 + 1
print(f'Alphabets: {c1}, digits: {c2}')

# Use list comprehension (Pythonic)
c3 = [i for i in s if i.isalpha()]
c4 = [i for i in s if i.isdigit()]
print(f'Alphabets: {len(c3)}, digits: {len(c4)}')

#%% Tuples
alist = [1, 2.3, 4+5j, 'abc', (1, 2, 3)]
atuple =(1, 2.3, 4+5j, 'abc', (1, 2, 3))

print(atuple[0])  # first item
print(atuple[-1])  # last item

print(f'{alist.__sizeof__()=}, {atuple.__sizeof__()=}')

alist[1] = -0.5  # change item at index 1
#atuple[1] = -0.5  # this will cause an error

a = [3]  # a list with a single item
b = (3,) # a tuple with a single item

#%% Dictionary
adict = {'happy': '😊', 'sad': '😢', 'neutral': '😑'}
print(adict['happy'])  # retrieve the value using key

adict['angry'] = '😠'  # add new key-value pair
print(f'{adict=}')

# Method 1 to create dictionary
d1 = {'x':1.2, 'y':2.3, 'z':4.5}

# Method 2 to create dictionary
alist = ['x', 'y', 'y']
blist = [1.2, 2.3, 4.5]
d2 = dict(zip(alist, blist))

# Method 3 to create dictionary
d3 = dict(x=1.2, y=2.3, z=4.5)

print(f'{d1=}, {d2=}, {d3=}')

#%% Methods for dictionary
d = dict(apple=1.2, banana=3.4, ciku=2.5, durian=25)
for k in d:
    print(f'{k=}')  # iterate by keys
    print(f'{k} is RM{d[k]:.2f}') 

d['egg'] = 4.75  # add new key-value pair
print(d['durian'])  # get the value for durian
#print(d['orange'])  # error
print(d.get('orange', 'not found'))  # It is better to use get method 

print(f'{d.keys()=}')  # to get all the keys
print(f'{d.values()=}')  # to get all the values
print(f'{d.items()=}')  # get all the key-value pairs

del d['ciku']  # remove the key-value pair for ciku
print(f'{d=}')
print(f'{len(d)=}')  # print the number of key-value pair in the dictionary

e = {'kiwi': 5.25, 'jambu': 2.5}
d.update(e)  # update d with contents from e
print(f'{d=}')
e.clear()  # clear the contents of e
print(f'{e=}')

# Create a new dictionary for new prices after 10% discount
# Method 1 - using for loop
n1 = {}
for k in d:
    n1[k] = d[k] * 0.9  # 10% discount
print(f'{d=}, {n1=}')

n2 = {k:d[k] * 0.9 for k in d}
print(f'{d=}, {n2=}')

adict = {'happy': '😊', 'sad': '😢', 'neutral': '😑', 'angry': '😠'}
bdict = {adict[k]:k for k in adict}  # reverse mapping using dictionary comprehension
print(f'{adict=}, {bdict=}')
print(bdict.get('😑'))
#%% alias, copy and deep copy
d1 = dict(a=1, b=3, c=5)
d2 = d1  # d2 is an alias of d1
print(f'{d1=}, {d2=}')
d1['d'] = 7
print(f'{d1=}, {d2=}')
d3 = d1.copy()
print(f'{d1=}, {d2=}, {d3=}')
del d1['b']
print(f'{d1=}, {d2=}, {d3=}')

d4 = dict(a=2, b=[4, 6, 8], c=10.12)
d5 = d4.copy()
d4['a'] = 3.5
print(f'{d4=}, {d5=}')

d4['b'][0] = -7
print(f'{d4=}, {d5=}')

from copy import deepcopy
d6 = deepcopy(d4)  # to create a deepcopy of d4
d4['b'][1] = -29
print(f'{d4=}, {d5=}, {d6=}')

#%% Functions
def make_polite(s):
    '''This is a function to improve the politeness of the sentence.
    Usage: make_polite(sentence) 
    E.g. print(make_polite("Buy  me a burger"))'''
    return s + ', please.'

help(make_polite)
print(make_polite.__doc__)

#%% Lambda function

ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id201', 'id125']
print(f'{sorted(ids)=}')

sorted_ids = sorted(ids, key=lambda x:int(x[2:]))
print(f'{sorted_ids=}')

#%% Using map()
a = list(range(2, 11, 2))

# Using list comprehension
b = [i**2 for i in a]

# Using map()
c = list(map(lambda x: x**2, a))

print(f'{b=}, {c=}')

animals = ['cat', 'panda', 'raccoon']

animals2 = [a.title() for a in animals]

animals3 = list(map(lambda x:x.title(), animals))

print(f'{animals2}, {animals3}')

#%% using filter()
a1 = [i for i in range(1, 101) if i % 3 == 0]  # using list comprehension
a2 = list(filter(lambda x: x % 3 == 0, range(1, 101)))  # using filter()
print(f'{a1=}, {a2=}')

animals = ['cat', 'panda', 'raccoon', 'horse']
animals2 = list(filter(lambda x: 'o' in x, animals))
print(f'{animals2}')
    