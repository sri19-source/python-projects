print("1. Kotak Bank")
print("2. ICICI Bank")
print("3. SBI Bank")
print("4. Axis Bank")
print("5. HDFC Bank")
print("6. Quit")

while True:
    choice = int(input("Enter your choice (1-6): "))


    if choice == 1:
        print("Kotak Bank offers 7% interest")
        rate = 7
    elif choice == 2:
        print("ICICI Bank offers 6.5% interest")
        rate = 6.5
    elif choice == 3:
        print("SBI Bank offers 6% interest")
        rate = 6
    elif choice == 4:
        print("Axis Bank offers 6.8% interest")
        rate = 6.8
    elif choice == 5:
        print("HDFC Bank offers 6.9% interest")
        rate = 6.9
    elif choice == 6:
        print("Thank you ")
        break
    else:
        print("Invalid choice")
        continue


    principal = float(input("Enter principal amount: "))
    time = float(input("Enter time in years: "))

    simple_interest = (principal * rate * time) / 100
    compound_interest = principal * (1 + rate/100) ** time - principal

    print("Simple Interest:", round(simple_interest,2))
    print("Compound Interest:", round(compound_interest,2))
