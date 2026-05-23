#multipliation table
num = int(input("Enter a number: "))
print("Multiplication Table of", num)
while num>0:
    for i in range(1, 11):
        print(num, "x", i, "=", num*i)
    break