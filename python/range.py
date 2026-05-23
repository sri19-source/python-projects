#temperature ranges
temp = float(input("Enter the temperature: "))

if temp < 0:
    print("Freezing weather")
elif temp <= 20:
    print("Cold weather")
elif temp <= 30:
    print("Warm weather")
else:
    print("Hot weather")