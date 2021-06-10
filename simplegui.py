# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 13:08:01 2020

@author: wooihaw
"""

#Class Task 1
class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def area(self):
        return self.l * self.w
    def perimeter(self):
        return 2*self.l + 2*self.w
    def __str__(self):
        return f'This is a rectangle with width {self.w} and length {self.l}'
    
rect1 = Rectangle(2, 3)
rect2 = Rectangle(4, 5)
print(rect1.area(), rect2.area())
print(rect1.perimeter(), rect2.perimeter())
print(rect1)
#%% Class Task 2
class Circle:
    def __init__(self, r=1):
        self.r = r
        self.__pi = 3.1412
    def area(self):
        return self.__pi * self.r ** 2
    def circumference(self):
        return 2 * self.__pi * self.r
    def __str__(self):
        return f'This is a circle with radius of {self.r}'

c1 = Circle()
c2 = Circle(3)
print(c1.area(), c2.area())
print(c1.circumference(), c2.circumference())
print(c1, c2)
print(c1.r, c2.r)
print(c1.__pi)
#%% An example of using numpy
import numpy as np
a = [1, 2, 3, 4, 5]
b = [5*i for i in a]
print(b)
c = np.array(a)
print(type(c))
d = 5 * c
print(d)
print(np.mean(a), np.median(a))

#%% Module & package
import s10_hello

import color

import color.htmlcodes as hc
print(hc.blue, hc.red)
#%% Basic GUI using tkinter
import tkinter as t
root = t.Tk()
root.mainloop()

#%% GUI with tkinter 
import tkinter as t
from tkinter import ttk

def on_click():
    print('You have clicked the button')
    
root = t.Tk()
root.title('My window')
root.geometry('400x400')
lbl = ttk.Label(root, text='Hello world').grid()
btn = ttk.Button(root, text='Quit', command=root.destroy).grid()
btn2 = ttk.Button(root, text='Click here', command=on_click).grid()
root.mainloop()

#%% Using easygui
import easygui as gui

ans = gui.ynbox(msg='Do you want to save the file?', title="To save or not to save", choices=['Y', 'N'])
print(ans)

fname = gui.fileopenbox(msg='Please select a file to open', title='Select file', default='*.txt')
print(fname)

ans2 = gui.msgbox(msg='Hello world. Python is fun!')
