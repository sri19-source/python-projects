list1=[1,2,3,4]
list1.append(5)
print(list1)  # [1, 2, 3, 4, 5]

list2=[6,7,8,9]
list2.insert(2, 5)
print(list2) # [6, 7, 5, 8, 9] 

list3=[10,11,12,13]
list3.extend([14, 15])
print(list3)  # [10, 11, 12, 13, 14, 15]

list4=[16,17,18,19]
list4.remove(18)
print(list4)  # [16, 17, 19]    

list5=[20,21,22,23]
list5.pop(3)
print(list5)  # [20, 21, 22, 23]

list6=[2,9,7]
list6.sort()
print(list6)  # [2, 7, 9]

list7=[3,1,4,2]
index1=list7.index(4)
print(index1)  # 2

list8=[5,6,7,8,6]
count1=list8.count(6)
print(count1)  # 2

list9=[10,20,30,40]
length1=len(list9)
print(length1)  # 4

list10=[1,2,84]
sum(list10)
print(sum(list10))  # 87