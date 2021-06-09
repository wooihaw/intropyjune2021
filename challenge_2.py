# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 14:23:29 2021

@author: wooihaw
"""
# Challenge 2
investment = eval(input('Enter the amount of investment: '))
interest = eval(input('Enter the interest rate (%): '))
duration = eval(input('Enter the duration of investment (years): '))

print(f'Initial investment: RM{investment:.2f}, annual rate: {interest}%, years of investment: {duration}')

for i in range(duration):
    investment = investment + investment * interest/100
    print(f'Year {i+1}: RM{investment:.2f}')