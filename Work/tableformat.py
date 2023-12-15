# -*- coding: utf-8 -*-

"""
Created on Fri Dec 15 12:18:56 2023

@author: loren
"""

# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()
        
class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))        
        
class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format.
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h:s}</th>', end='')
        print('<tr>')
    
    def row(self, rowdata):
        print('<tr>', end='')
        for r in rowdata:
            print(f'<td>{r:s}</td>', end='')
        print('<tr>')
        
        
def create_formatter(name):
    '''
    Create an appropriate formatter given an output format name
    '''
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise ValueError(f'Unknown table format {name}')
        
        
        
def print_table(objects, headers, formatter):
    formatter.headings(headers)
    for obj in objects:
        rowdata = [ str(getattr(obj, name)) for name in headers]
        formatter.row(rowdata)
    
        