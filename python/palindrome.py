#palindrome number
num=int(input("enter a number:"))
temp=num
rev=0
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp//=10
if num==rev:
    print("palindrome")
else:
    print("not palindrome")