# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 16:32:18 2021

@author: wooihaw
"""
# Challenge 12
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/covid19.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

print(df)

cases_5000 = df['Case'] > 5000
print(f'There are {sum(cases_5000)} days with more than 5000 cases')
print(df[cases_5000])

deaths_50 = df['Death'] > 50
print(f'There are {sum(deaths_50)} days with more than 50 deaths')
print(df[deaths_50])

# Plot bar chart for cases per month
m_groups = df.groupby(df.index.to_period('M'))
