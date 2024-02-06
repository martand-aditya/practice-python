# mortgage.py
#
# Exercise 1.7
principal = 500000
rate = 0.05
total_paid = 0
payment = 2684.11
months = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000


while principal > 0:
    
    months +=1
    
    if principal < payment:
        principal = principal * (1+rate/12)
        total_paid = total_paid + principal
        principal = 0
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        
    
    if months >= extra_payment_start_month and months <= extra_payment_end_month:

        principal = principal -extra_payment
        total_paid = total_paid + extra_payment


    print(months, round(total_paid,2), round(principal,2))



print('Total Paid',round(total_paid,2))
print('Total Months',months)