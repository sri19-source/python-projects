#sales commision calculator
print("Welcome to the sales commission calculator!")
sales_amount = float(input("Enter the total sales amount : "))
if sales_amount > 10000:
     commission_rate = 0.10
elif sales_amount > 5000:
    commission_rate = 0.07
elif sales_amount > 1000:
    commission_rate = 0.05
else:
     commission_rate = 0.02
commission = sales_amount * commission_rate
print(f"The commission for a sales amount of {sales_amount:.2f} is {commission:.2f}.")
total=sales_amount+commission
print(f"The total amount including commission is {total:.2f}.")