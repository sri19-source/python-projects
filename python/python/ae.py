def evaluate_expression(x, a, b, c):
    result = (a * x ** 2) + (b * x) + c
    return result

a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))
c = int(input("Enter a value for c: "))
x = float(input("Enter a value for x: "))

result = evaluate_expression(x, a, b, c)
print("The result of the expression ax^2 + bx + c is:",a, "x^2 +", b, "x +", c, "=")
print("The result of the expression ax^2 + bx + c is:", result)
