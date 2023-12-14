# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
total_months = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

i=0


while principal > 0:
    if extra_payment_start_month <= total_months and total_months <= extra_payment_end_month :
        extra_payment = 1000
    else:
        extra_payment = 0    
    principal = principal * (1+rate/12) - payment - extra_payment
    total_paid = total_paid + payment + extra_payment
    total_months += 1 
    if principal < 0:
        total_paid = total_paid + principal
        principal = 0
    print(total_months, f'{total_paid:0.2f} {principal:0.2f}')

print(f'Total paid: {total_paid:0.2f}')
print('Total time to pay it:', total_months)



