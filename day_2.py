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

print(b is a)  # check whether b is an alias of a
print(b == a)  # check whether b has the same contents as a