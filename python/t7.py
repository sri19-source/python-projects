n=int(input("enter the n value:"))
count=0
t=0
while n!=0:
    r=n%10
    t+=1
    n//=10
print("t value:",t)
