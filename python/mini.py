#mini investment calculator
initial_investment = float(input("Enter the initial investment amount: "))
annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
investment_duration_years = int(input("Enter the investment duration (in years): "))
final_amount = initial_investment * (1 + annual_interest_rate / 100) ** investment_duration_years
print(f"Final amount after {investment_duration_years} years: {final_amount:.2f}")
