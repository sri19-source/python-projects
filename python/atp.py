#random otp geneator and validation 
import random
otp = random.randint(1000, 9999)
print("Your OTP is:", otp)
user_otp = int(input("Enter the OTP: "))
if user_otp == otp:
    print("OTP is valid. Access granted.")
else:
    print("OTP is invalid. Access denied.")
