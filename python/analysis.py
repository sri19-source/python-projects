#include student  marks analysis  system
name=input("Enter your name: ")
maths=int(input("Enter your  math marks: "))
science=int(input("Enter your science marks: "))
english=int(input("Enter your english marks: "))
total_marks=((maths+science+english)//300)*100
if total_marks>=90:
    grade='A'   
elif total_marks>=80:
    grade='B'
elif total_marks>=70:
    grade='C'
elif total_marks>=60:
    grade='D'
else:
    grade='F'
print(f"{name}, your grade is: {grade}")
