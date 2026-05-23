import random
number=random.randint(1,500)
count=0
guess=0
while guess!=number and count<10:
    guess=int(input("enter your guessed number:"))
    count+=1
    if guess<number:
        print("too low")
    elif guess>number:
        print("too high")
if guess==number:
    print(f"congraculations you have guessed the number {number} in {count}attempts")
else:
    print(f"you lost ,the number of counts{count} exceeded and the number is {number}")
    
