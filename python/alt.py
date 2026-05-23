#Compute alternating series (1 − 2 + 3 − 4 …).
n=int(input("enter the number of terms:"))
sum=0
for i in range(1,n+1):
    if i%2==0:
        sum=sum-i
    else:
        sum=sum+i
print("the sum of the series is:",sum)