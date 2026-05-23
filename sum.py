array=[]
i=0
n=int(input("number of array elements:"))
while i<=n:
    x=int(input("enter a number:"))
    array.append(x)
    i+=1
target=int(input("enter the target number:"))
for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i]+array[j]==target:
            print(f"[{i},{j}]")
