#income tax calculation
name=input("Enter your name: ")
income=int(input("Enter your annual income: "))
"""0 - ₹4 Lakh: Nil
₹4,00,001 - ₹8,00,000: 5%
₹8,00,001 - ₹12,00,000: 10%
₹12,00,001 - ₹16,00,000: 15%
₹16,00,001 - ₹20,00,000: 20%
₹20,00,001 - ₹24,00,000: 25%
Above ₹24,00,000: 30%"""
if income<=400000:
    tax=0
elif income<=800000:
    tax=income*0.05
elif income<=1200000:
    tax=income*0.10
elif income<=1600000:
    tax=income*0.15
elif income<=2000000:
    tax=income*0.20
elif income<=2400000:
    tax=income*0.25
else:    tax=income*0.30
print(f"{name}, your income tax is: ₹{tax}")
