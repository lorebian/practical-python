# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 09:58:19 2023

@author: loren
"""

# stock.py
# Exercise 4.1
from .typedproperty import typedproperty

class Stock:
    String = lambda name: typedproperty(name, str)
    Integer = lambda name: typedproperty(name, int)
    Float = lambda name: typedproperty(name, float)
   
    name = String('name')
    shares = Integer('shares')
    price = Float('price')
    
   
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        
    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'
    
    @property
    def cost(self):
        return self.shares * self.price

        
    def sell(self, nshares):
        self.shares -= nshares
     
        
class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        # Check the call to `super` and `__init__`. If __init__ is redefined, it is essential to initialize the parent.  
        super().__init__(name, shares, price)
        self.factor = factor
    
    
    def panic(self):
        self.sell(self.shares)
        
    def cost(self):
        # Check the call to `super`, it calls the previous version.
        return self.factor * super().cost()
         
class NewStock(Stock):
        def yow(self):
            print('Yow!')