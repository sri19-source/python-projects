#shopping discount
print("Welcome to the shopping discount calculator!")
while True:
    print('enter the section of the item you want to buy')
    print("1.Electronics \n 2.Clothing \n 3.Groceries \n 4.Home Appliances \n 5.Books \n 6.exit")
    choice = int(input("Enter your choice (1-6): "))
    if choice == 1:
        print("You have selected Electronics.")
        discount_percentage = 15
    elif choice == 2:
        print("You have selected Clothing.")
        discount_percentage = 10
    elif choice == 3:
        print("You have selected Groceries.")
        discount_percentage = 5
    elif choice == 4:
        print("You have selected Home Appliances.")
        discount_percentage = 12
    elif choice == 5:
        print("You have selected Books.")
        discount_percentage = 8
    elif choice == 6:
        print("Thank you for using the shopping discount calculator. Goodbye!")
        break
    
    original_price = float(input("Enter the original price of the item: "))
    discount_amount = (discount_percentage / 100) * original_price
    final_price = original_price - discount_amount
    print(f"The final price of the item is {final_price:.2f}.") 

