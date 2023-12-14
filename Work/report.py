# report.py
#
# Exercise 2.4 / Exercise 2.5

import csv
from pprint import pprint
import fileparse as fp

def read_portfolio(filename):  
    portfolio = []
    file_open = False
    if type(filename) is str:
        file = open(filename,  'rt')
        file_open = True
    else:
        file = filename
    rows = csv.reader(file)
    headers = next(rows)
    for rowno, row in enumerate(rows, start =1):
        record = dict(zip(headers, row))
        try:
            name = record['name']
            nshares = int(record['shares'])
            price = float(record['price'])
            holding = {'name': name, 'shares': nshares, 'price' : price}
            portfolio.append(holding)
        except ValueError:
            print(f'Row {rowno}: Bad row: {row}')
    if file_open:
        file.close()
    return portfolio


# Exercise 2.6

def read_prices(filename):
    'Reads a set of prices into a dict'
    dict_prices = {}
    file_open = False
    if type(filename) is str:
        file = open(filename,  'rt')
        file_open = True
    else:
        file = filename
    rows = csv.reader(file)
    for row in rows:
        try:
            dict_prices[row[0]] = float(row[1])
        except:
            print('Error')
    if file_open:
        file.close()
    return dict_prices 

#prices = read_prices('Data/prices.csv') 


# Exercise 2.7: computing gain/loss of shares with updated price

# total_newprices = 0
# for s in portfolio:
#     total_newprices += s['shares']*prices[s['name']]     
# print(total_newprices)

# difference = total_newprices - total_portfolio 

# if difference > 0:
#     print( f'You rock! You have gained ${difference:0.2f}')
# else:
#     print(f'Oh no! You have lost ${abs(difference):0.2f}') 
    
# Exercise 2.9 

def make_report(portfolio_file, prices_file):
    'returns a list of tuples with the rows: Name, Shares, Price, Change'
    portfolio = fp.parse_csv(portfolio_file, types=[str, int, float])
    prices = dict(fp.parse_csv(prices_file, types=[str,float], has_headers=False))
    rows_report = []
    for s in portfolio:        
        rows_report.append((s['name'], s['shares'], prices[s['name']], prices[s['name']]-s['price']))        
    print_report(rows_report)
    return rows_report
   

def print_report(report):   
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
        form_price = '%0.2f' % price
        str_price = '$' + str(form_price)
        print(f'{name:>10s} {shares:>10d} {str_price:>10s} {change:>10.2f}')
    

def portfolio_report(portfolio_filename, prices_filename):
    make_report(portfolio_filename,prices_filename)
    
       
def main(args):
    if len(args) != 3:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfolio_filename price_filename')
    portfolio_report(args[1], args[2])

    
if __name__ == '__main__':
    import sys
    main(sys.argv)        













    