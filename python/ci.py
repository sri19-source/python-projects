#Compute compound interest repeatedly for years
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = int(input("Enter the number of years: "))
amount = principal * (1 + rate / 100) ** time
print(f"Amount after {time} years: {amount:.2f}")