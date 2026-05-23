# Create a menu-driven student database (basic version without loops)

roll = int(input("Enter the roll number to search (1-5): "))

match roll:
    case 1:
        print("Roll Number: Y25CB001")
        print("Name: Alice")
        print("Age: 20")
        print("Grade: A")
    case 2:
        print("Roll Number: Y25CB002")
        print("Name: Bob")
        print("Age: 21")
        print("Grade: B")
    case 3:
        print("Roll Number: Y25CB003")
        print("Name: Charlie")
        print("Age: 22")
        print("Grade: C")
    case 4:
        print("Roll Number: Y25CB004")
        print("Name: David")
        print("Age: 23")
        print("Grade: D")
    case 5:
        print("Roll Number: Y25CB005")
        print("Name: Eve")
        print("Age: 24")
        print("Grade: F")
    case _:
        print("Student not found in the database.")


