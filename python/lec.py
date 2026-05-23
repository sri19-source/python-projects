#electricity triff calculation
units_consumed = float(input("Enter the number of units consumed: "))
n=int(input("Enter the number of days after which the bill is paid: "))
if units_consumed <= 100:
    bill_amount = units_consumed * 0.5
elif units_consumed <= 200:
    bill_amount = 100 * 0.5 + (units_consumed - 100) * 0.75
elif units_consumed <= 300:
    bill_amount = 100 * 0.5 + 100 * 0.75 + (units_consumed - 200) * 1.20
else:
    bill_amount = 100 * 0.5 + 100 * 0.75 + 100 * 1.20 + (units_consumed - 300) * 1.50
print(f"Total electricity bill amount: {bill_amount:.2f}")
tariff=bill_amount+(bill_amount*0.10*n)
print(f"Total bill amount after {n} days: {tariff:.2f}")