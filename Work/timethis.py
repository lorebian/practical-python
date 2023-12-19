# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 20:02:47 2023

@author: loren
"""

# timethis.py
import time

def timethis(func):   # wraps a function 
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print('%s.%s: %f' % (func.__module__, func.__name__, end-start))
       
    return wrapper


# @logged
# def add(x, y):
#     return x + y