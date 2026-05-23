# amount in saving account is 10000000
# amount in current account is 5000000

print("Welcome to the ATM!")

card_number = input("Please insert your card (enter card number): ")
pin = input("Please enter your PIN: ")

if len(pin) == 4 and pin == "5264":
    print("PIN accepted. Please proceed.")
    
    print("Select Transaction Type:")
    print("1. Withdrawal")
    transaction_type = input("Enter the number corresponding to your transaction type: ")
    
    if transaction_type == "1":
        print("Select Account Type:")
        print("1. Savings")
        print("2. Current")
        account_type = input("Enter the number corresponding to your account type: ")
        
        if account_type == "1":
            account_name = "Savings"
            balance = 10000000
        elif account_type == "2":
            account_name = "Current"
            balance = 5000000
        else:
            print("Invalid account type selected.")
            exit()
        
        amount = float(input("Enter the amount to withdraw: "))
        
        if amount > balance:
            print("Insufficient funds.")
        else:
            balance -= amount
            print(f"Processing your withdrawal of ₹{amount} from your {account_name} account...")
            print(f"Remaining balance: ₹{balance}")
            print("Please take your cash and card. Thank you for using our ATM!")
    else:
        print("Invalid transaction type.")
else:
    print("Invalid PIN. Please try again.")