#dice rolling and propability
import random
enter = input("Press Enter to roll the dice...")
if enter == "":
    dice_roll = random.randint(1, 6)
    print(f"You rolled a {dice_roll}!")
probability = 1/6
print(f"The probability of rolling a {dice_roll} is {probability:.2f}")
times = int(input("How many times do you want to roll the dice? "))
rolls = [random.randint(1, 6) for _ in range(times)]
print(f"You rolled: {rolls}")
probability_times= rolls.count(dice_roll) / times
print(f"The probability of rolling a {dice_roll} in {times} rolls is {probability_times:.2f}")