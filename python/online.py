#online shopping discount
print("Welcome to the online shopping discount calculator!")
while True:
    item_name = input("Enter the name of the item :")

    if item_name == "quit":
        print("Thank you for using the online shopping discount calculator. Goodbye!")
        break
    original_price = float(input("Enter the original price of the item: "))
    if original_price>5000:
        print("u get 20% discount")
        discount_percentage = 20
    elif original_price>2000:
        print("u get 10% discount")
        discount_percentage = 10
    elif original_price>1000:
        print("u get 5% discount")
        discount_percentage = 5
    else:
        print("No discount available.")
        discount_percentage = 0
    discount_amount = (discount_percentage / 100) * original_price
    final_price = original_price - discount_amount
    print(f"The final price of {item_name} is {final_price:.2f}.")