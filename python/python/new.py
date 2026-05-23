num=input("Enter a number:")
num1=input("Enter another number:")

comparsion=None
match comparsion:
    case equal if num == num1:
        print("Both numbers are equal.")
    case greater if num > num1:
        print(f"{num} is greater than {num1}.")
    case less if num < num1:
        print(f"{num} is less than {num1}.")
    case _:
        print("Invalid input or comparison not recognized.")
