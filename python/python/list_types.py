#example1
list1=[6,9,8,5]
list1.append(4)
print(list1)   # [6, 9, 8, 5, 4]

#example2
list2=[1,2,8,7] 
list2.insert(3, 4)    
print(list2)  # [1, 2, 8, 4, 7]

#example3       
list3=[10,11,12,13]
list3.extend([1, 2])
print(list3)  # [10, 11, 12, 13, 1, 2]

#example4
list4=[16,17,18,20]
list4.remove(18)
print(list4)  # [16, 17, 20]

#example5
list5=[20,21,22,23]
list5.pop(3)
print(list5)  # [20, 21, 22]    

#example6
list6=[2,9,7]   
list6.sort()
print(list6)  # [2, 7, 9]

#example7
list7=[3,1,4,2]
index1=list7.index(4)
print(index1)  # 2

#example8
list8=[5,6,7,8,6]
count1=list8.count(6)
print(count1)  # 2

#example9
list9=[10,20,30,40] 
length1=len(list9)
print(length1)  # 4

#example10
list10=[1,2,84] 
total_sum=sum(list10)
print(total_sum)  # 87

#example11
list11=[1,45,65]
max_value=max(list11)
print(max_value)  # 65

#example12
list12=[45,67,83]
min_value=min(list12)
print(min_value)  # 45

#example13
list13=[1,2,3,4]
list13.clear()
print(list13)  # []

#example14
list14=[1,2,3,4]
list14.reverse()
print(list14)  # [4, 3, 2, 1]

