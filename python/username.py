import random

name = input("Enter your full name: ")

# remove spaces and make lowercase
base = name.replace(" ", "")

symbols = [".", "_"]
number = random.randint(10, 999)

username = base + random.choice(symbols) + str(number)

print("Your username is:", username)