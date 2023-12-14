# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select = None, types = None, has_headers=True, delimiter = None, silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    file_open = False
    if type(filename) is str:
        file = open(filename,  'rt')
        file_open = True
    else:
        file = filename
    if delimiter:
        rows = csv.reader(file, delimiter=' ') 
    else:           
        rows = csv.reader(file)        
    records = []
    if has_headers:           
        # Reading file headers
        headers = next(rows)
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []
        for rowno, row in enumerate(rows, start=1):
            if not row:  # Skip rows with no data
                continue           
            if indices:
                row = [row[index] for index in indices]
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]                                      
                except ValueError as e:
                    if silence_errors:
                        continue
                    else:
                        print(f'Row {rowno}: Couldn\'t convert {row}') 
                        print(f'Row {rowno}: Reason',e)     
            # Make a dict    
            record = dict(zip(headers, row))
            records.append(record)
    else:
        if select:
            raise RuntimeError("select argument requires column headers")
        else:
            for rowno, row in enumerate(rows, start=1):
                if not row:  # Skip rows with no data
                    continue
                if types:
                    try:
                        row = [func(val) for func, val in zip(types, row)]
                    except ValueError as e:
                        if silence_errors:
                            continue
                        else:
                            print(f'Row {rowno}: Couldn\'t convert {row}') 
                            print(f'Row {rowno}: Reason',e)
                record = tuple(row)    
                records.append(record)            
    if file_open:
        file.close()
    return records

# shares_held = parse_csv('Data/portfolio.csv', select=['name','shares'])
# prices = parse_csv('Data/prices.csv', types=[str,float], has_headers=False)
# portfolio = parse_csv('Data/portfolio.dat', types=[str, int, float], delimiter=' ')
# prices = parse_csv('Data/prices.csv', select=['name','price'], has_headers=False)
# portfolio = parse_csv('Data/missing.csv', types=[str, int, float])
# portfolio = parse_csv('Data/missing.csv', types=[str,int,float], silence_errors=True)