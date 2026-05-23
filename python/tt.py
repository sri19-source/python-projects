#triangle types 
a = int(input("Enter the first side of the triangle: "))
b = int(input("Enter the second side of the triangle: "))
c = int(input("Enter the third side of the triangle: "))
if a == b == c:
    print("The triangle is equilateral.")
elif a == b or b == c or a == c:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")
x=int(input("Enter the first angle of the triangle: "))
y=int(input("Enter the second angle of the triangle: "))
z=int(input("Enter the third angle of the triangle: "))
if x==90 or y==90 or z==90:
    print("The triangle is right-angled.")
elif x>90 or y>90 or z>90:
    print("The triangle is obtuse-angled.")
else:
    print("The triangle is acute-angled.")
