#email format validation
email = input("Enter email: ")
if email.count("@") == 1 and "." in email and " " not in email and len(email) >= 5 and email.index("@") > 0 and email.index(".") > email.index("@") + 1 and email.index(".") < len(email) - 1:
    print("Valid email format")
else:
    print("Invalid email")