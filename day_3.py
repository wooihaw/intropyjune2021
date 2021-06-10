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
    outfile.write('We are appending to the file.\n')

#%% File reading
with open('test.txt', 'r') as f:
    s1 = f.read(5)  # reading the first 5 characters
    s2 = f.read(10) # reading the next 10 characters
    print(f'{s1=}, {s2=}')
    f.seek(0)  # rewind back to position 0 (beginning of the file)
    s3 = f.read(10)  # reading the first 10 characters
    f.seek(15) # forward to position 15
    s4 = f.read(5)  # read 5 characters
    print(f'{s3=}, {s4=}')
    f.seek(0)
    line1 = f.readline()
    line2 = f.readline()
    print(f'{line1=} {line2=}')
    f.seek(0)
    lines = f.readlines()
    print(f'{lines=}')
    f.seek(0)
    s = f.read()
    print(f'{s=}')
    
#%% Iterate through file
with open('test.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line)

with open('test.txt', 'r') as f:
    for line in f:
        print(line)

#%% Writing UTF-8 encoded file
contents = '''😊😂🤣😢😑😠
👌👍✌👏
🍕🍔🍟🌭🍿'''

with open('emoji.txt', encoding='utf-8', mode='w') as f:
    f.write(contents)
    
#%% Reading UTF-8 encoded file
with open('emoji.txt', encoding='utf-8', mode='r') as g:
    s = g.read()
print(f'{s=}')

#%% Write to multiple lines
alist = ['This is line 1', 'This is line 2', 'This is line 3']
with open('multilines.txt', 'w') as f:
    f.writelines(alist)
