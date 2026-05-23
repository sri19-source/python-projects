#salary breakup calculator
#hra is house rent allowance and da is dearness allowance d
basic_salary = float(input("Enter your basic salary: "))
hra = 0.20 * basic_salary
da = 0.10 * basic_salary
gross_salary = basic_salary + hra + da
print(f"Basic Salary: {basic_salary:.2f}")
print(f"HRA: {hra:.2f}")
print(f"DA: {da:.2f}")
print(f"Gross Salary: {gross_salary:.2f}")
