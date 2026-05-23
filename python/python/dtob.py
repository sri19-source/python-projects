#decimal to binary conversion
decimal_number = int(input("Enter a decimal number: "))
while decimal_number > 0:
     binary_digit = decimal_number % 2
     print(binary_digit)
     decimal_number = decimal_number // 2
print(" the decimal number is converted to binary")

