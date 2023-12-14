# pcost.py
#
# Exercise 1.27

import csv
import report
   
def portfolio_cost(filename):
    'Calculates total cost of a portfolio'
    total_cost = 0
    record = report.read_portfolio(filename)
    for item in record: 
        try: 
            #total_payed = total_payed + int(row[1])*float(row[2])
            nshares = int(item['shares'])
            price = float(item['price'])
            total_cost += nshares * price
        #This catches errors in int() and float() conversions above    
        except ValueError:
              print('Missing values, bad row.')
    #f.close()
    print(f'Total cost {total_cost:0.2f}')
    return total_cost


def main(args):
    if len(args) != 2:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfolio_filename')
    portfolio_cost(args[1])

    
if __name__ == '__main__':
    import sys
    main(sys.argv)       
            