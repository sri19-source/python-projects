#attendence checker
print("total number of days a college is open: 300")
total_days = 365
present_days = int(input("Enter the number of days the student was present: "))
attendance_percentage = (present_days / total_days) * 100
print(f"Attendance percentage: {attendance_percentage:.2f}%")
if attendance_percentage >= 75:
    print("The student is allowed to sit in the exam.")
else:
    print("The student is not allowed to sit in the exam.")
    