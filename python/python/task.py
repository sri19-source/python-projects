"""🚧 Your Task:
Write a Python script that:

Stores the name, age, and 3 subject marks of a student using variables.

Calculates the total marks and average.

Checks if the student passed or failed using comparison operators.

Uses assignment operators (+=, -=, etc.) at least once.

Prints the results clearly using print() and maybe some comments for readability."""

name="gwen" 

age=17

maths=80

physics=60

chemistry=60

total=(maths+chemistry+physics)

print(total)

average=total/3

print(average)

if average >=50:
    print(f"{name} has passed with an average of {average}")
else:
    print(f"{name} has failed with an average of {average}")

 

