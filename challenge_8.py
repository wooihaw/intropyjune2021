# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 15:50:03 2021

@author: wooihaw
"""
# Challenge 8
class Circle:
    def __init__(self, r=1):
        self.r = r
        self.__pi = 3.1412
    
    def area(self):
        return self.__pi * self.r ** 2
    
    def circumference(self):
        return 2 * self.__pi * self.r
    
if __name__ == '__main__':
    c1 = Circle(4)
    print(f'Area={c1.area()}, circumference={c1.circumference()}')