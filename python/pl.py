#profit and loss calculation
cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))
if selling_price > cost_price:
    profit = selling_price - cost_price
    print(f"You made a profit of: {profit:.2f}")
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print(f"You incurred a loss of: {loss:.2f}")
else:
    print("No profit, no loss.")