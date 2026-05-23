#scolarship elegibility checker
name=input("Enter the student's name: ")
grade=float(input("Enter the student's grade (0-100): "))
#Academic Performance: Minimum 55% or 60% marks in the qualifying examination (e.g., Class 10th, 12th, or graduation).
income=float(input("Enter the family's annual income in INR: "))
age=int(input("Enter the student's age: "))
documents=input("Does the student have all the required documents? (yes/no): ").lower()
caste=input("Enter the student's caste (General/SC/ST/OBC): ").lower()
if grade >= 55 and income <= 500000 and age <= 25 and documents == "yes" and caste in ["sc", "st", "obc"]:
    print(f"{name} is eligible for the scholarship of 100000 INR.")
elif grade >= 60 and income <= 300000 and age <= 25 and documents == "yes" and caste == "general":
    print(f"{name} is eligible for the scholarship of 50000 INR.")
else:
    print(f"{name} is not eligible for the scholarship.")
