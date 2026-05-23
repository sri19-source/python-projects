# EMI Calculator
def calculate_emi(principal, rate, time):
    emi = (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
    return emi

p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))    
t = float(input("Enter the time in years: "))
emi = calculate_emi(p, r, t)
print("The EMI is:", emi)  