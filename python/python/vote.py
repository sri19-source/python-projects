#voting
def vote(age):
    person = input("which country are you from? ")
    if person == "India":
        if age >= 18:
           return "You are eligible to vote."
        else:
           return "You are not eligible to vote yet."
    else:
        return "Sorry, this program is only for Indian citizens."
    

age = int(input("Enter your age: "))
result = vote(age)
print(result)