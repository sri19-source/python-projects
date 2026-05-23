#number guessing game
import random
number = random.randint(1, 100)
count=0
guess=0
while guess!=number and count<10:
    guess=int(input("Enter your guess: "))
    count+=1
    if guess<number:
        print("Too low!")
    elif guess>number:
        print("Too high!")
if guess==number:
    print(f"Congratulations! You guessed the number in {count} attempts.")
else:
    print(f"Sorry, you've used all your attempts. The number was {number}.")    