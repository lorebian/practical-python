# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 09:58:19 2023

@author: loren
"""

# stock.py
# Exercise 4.1

class Stock:
    __slots__ = ('name','_shares','price')
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
    
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value     
        
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