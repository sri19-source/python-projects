#gcd
a=int(input("enter a number:"))
b=int(input("enter another number:"))
while a!=b:
    if a>b:
        a-=b
    else:
        b-=a
print("GCD:", a)