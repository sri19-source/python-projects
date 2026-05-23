#currency convertor
amount = float(input("Enter the amount in rupees: "))
print("Select the currency to convert to:")
print("1. US Dollar (USD) \n 2. Euro (EUR) \n 3. British Pound (GBP) \n 4. Japanese Yen (JPY) \n 5. Australian Dollar (AUD)")
choice = int(input("Enter your choice (1-5): "))
if choice == 1:
    converted_amount = amount * 0.0109
    print(f"{amount} rupees is equal to {converted_amount:.2f} US Dollars.")
elif choice == 2:
    converted_amount = amount * 0.0094
    print(f"{amount} rupees is equal to {converted_amount:.2f} Euros.")
elif choice == 3:
    converted_amount = amount * 0.0081
    print(f"{amount} rupees is equal to {converted_amount:.2f} British Pounds.")
elif choice == 4:
    converted_amount = amount * 1.71
    print(f"{amount} rupees is equal to {converted_amount:.2f} Japanese Yen.")
elif choice == 5:
    converted_amount = amount * 0.0155
    print(f"{amount} rupees is equal to {converted_amount:.2f} Australian Dollars.")