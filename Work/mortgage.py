# mortgage.py
#
# Exercise 1.7
# Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s
# Mortgage, Stock Investment, and Bitcoin trading corporation. The interest rate is 5%
# and the monthly payment is $2684.11.

tenure_years = 30
principal = 500_000
annual_rate = 0.05
monthly_paid_amount = 2684.11
total_paid_amount = 0

while principal > 0:
    principal = principal * (1 + annual_rate / 12) - monthly_paid_amount
    total_paid_amount += monthly_paid_amount

print("Total paid amount: ", round(total_paid_amount, 5))
