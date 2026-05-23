#compound intrest
def compound_interest(principal, rate, time):
    amount = principal * (pow((1 + rate / 100), time))
    ci = amount - principal
    return ci
p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))    
t = float(input("Enter the time in years: "))
ci = compound_interest(p, r, t)
print("The compound interest is:", ci)  
