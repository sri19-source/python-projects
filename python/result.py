#result anaylysis system of a student
name=input("Enter the name of the student:")
marks1=float(input("Enter the marks of subject 1:"))
marks2=float(input("Enter the marks of subject 2:"))
marks3=float(input("Enter the marks of subject 3:"))
marks4=float(input("Enter the marks of subject 4:"))
marks5=float(input("Enter the marks of subject 5:"))
total_marks=marks1+marks2+marks3+marks4+marks5
percentage=(total_marks/500)*100
print(f"Total marks obtained by {name} is {total_marks:.2f} out of 500.")
print(f"Percentage obtained by {name} is {percentage:.2f}%.")
if percentage >= 90:
    print("Grade: A")
    print("Excellent performance! Keep up the good work!")
elif percentage >= 80:
    print("Grade: B")
    print("Good job! You can aim for an A next time with a little more effort.")
elif percentage >= 70:
    print("Grade: C")
    print("You're doing well! Keep up the good work.")
elif percentage >= 60:
    print("Grade: D")
    print("You're on the right track! Keep working hard.")
else:
    print("Grade: F")
    print("You need to work harder to improve your performance.")