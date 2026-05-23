#traffic fine calculator
print('1.speeding \n 2.not wearing helmet \n 3.double parking \n 4.carrying more than 2 persons')
if input("Enter the traffic violation (1-4): ") == "1": 
    print("You have been fined for speeding.")
    speed = int(input("Enter the speed of the car: "))
    if speed <= 60:
        print("No fine. You are within the speed limit.")
    elif speed <= 80:
        print("Fine: ₹100. You are exceeding the speed limit by 1-20 km/h.")
    elif speed <= 100:
        print("Fine: ₹200. You are exceeding the speed limit by 21-40 km/h.")
    elif speed <= 120:
        print("Fine: ₹300. You are exceeding the speed limit by 41-60 km/h.")
    else:
        print("Fine: ₹500. You are exceeding the speed limit by more than 60 km/h.")
elif input("Enter the traffic violation (1-4): ") == "2":
        print("You have been fined for not wearing a helmet.")
        print("Fine: ₹200. You are not wearing a helmet.")
elif input("Enter the traffic violation (1-4): ") == "3":
        print("You have been fined for double parking.")
        print("Fine: ₹300. You are double parked.")
elif input("Enter the traffic violation (1-4): ") == "4":
    print("You have been fined for carrying more than 2 persons.")
    print("Fine: ₹400. You are carrying more than 2 persons.")
else:    print("Invalid traffic violation. Please enter a number between 1 and 4.")