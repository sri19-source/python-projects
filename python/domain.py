#which domain
email = input("Enter email: ")
if "@" in email :
    domain = email.split("@")[1]
    print(f"The domain  is: {domain}")