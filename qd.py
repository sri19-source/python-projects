print("the quadratic equation is ax^2 + bx + c = 0")
a,b,c=map(float,input("Enter the coefficients a, b, and c separated by spaces: ").split())
print("The quadratic equation is: {}x^2 + {}x + {} = 0".format(a, b, c))
d = b**2 - 4*a*c
if d > 0:
    x1 = (-b + d**0.5) / (2*a)
    #X=-B+/-sqrt(D)/2A
    x2 = (-b - d**0.5) / (2*a)
    print("The roots are real and different")
    print("x1 =", x1)
    print("x2 =", x2)
elif d == 0:
    x = -b / (2*a)
    print("The roots are real and equal")
    print("x =", x)
else:
    print("The roots are complex")
    real_part = -b / (2*a)
    imaginary_part = (abs(d)**0.5) / (2*a)
    print("x1 =", real_part, "+", imaginary_part, "i")
    print("x2 =", real_part, "-", imaginary_part, "i")