# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 15:06:52 2023

@author: loren
"""

# sears.py

bill_thikness = 0.11 * 0.001 # in meters (0.11 mm)
sears_height = 442 # height in meters
num_bills = 1
day = 1

while num_bills * bill_thikness < sears_height:
    print(day, num_bills, num_bills * bill_thikness)
    day += 1
    num_bills *= 2
    

print('Number of days:', day)
print('Number of bills:', num_bills)
print('Final height:', num_bills * bill_thikness)
    
