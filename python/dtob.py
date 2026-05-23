#decimal to binary
num = int(input("Enter a number: "))
binary=""
while num > 0:
    rem = num % 2
    binary = str(rem) + binary
    num //= 2
print("Binary representation:", binary)