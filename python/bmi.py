#BMI category analyzer with health advice.
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")
if bmi < 18.5:
    print("You are underweight. Consider a balanced diet and regular exercise to gain weight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight. Maintain a healthy lifestyle with a balanced diet and regular exercise.")
elif 25 <= bmi < 29.9:
    print("You are overweight. Consider a healthy diet and regular exercise to lose weight.")
else:
    print("You are obese. It is important to consult a healthcare professional for personalized advice on weight management and overall health.")