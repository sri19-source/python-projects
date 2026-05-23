#radom password genarotor
import random
password_length = int(input("Enter the desired password length: "))
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
password = "".join(random.choice(characters) for _ in range(password_length))
print("Generated password:", password)