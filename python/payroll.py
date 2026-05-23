#mini payroll system
while True:
    print("Welcome to the payroll system!")
    id=input("Enter the employee ID: ")
    employee_name = input("Enter the employee's name: ")
    salary = float(input("Enter the employee's salary: "))
    hra = salary * 0.20
    da = salary * 0.10
    pf = salary * 0.12
    tax = salary * 0.05
    net_salary = salary + hra + da - pf - tax
    print(f"Salary Slip for {employee_name} (ID: {id})")
    print(f"Basic Salary: {salary:.2f}")
    print(f"HRA: {hra:.2f}")
    print(f"DA: {da:.2f}")
    print(f"PF: {pf:.2f}")
    print(f"Tax: {tax:.2f}")
    print(f"Net Salary: {net_salary:.2f}")
    cont = input("Do you want to enter details for another employee? (yes/no): ")
    if cont.lower() != "yes":
        print("Thank you for using the payroll system. Goodbye!")
        break
    
    
