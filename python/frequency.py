string=input("Enter a string: ")
character=input("Enter the character to find its frequency: ")
count=0
for char in string:
    if char==character:
        count+=1
print(f"The frequency of '{character}' in the string is: {count}")
# print(f"The frequency of '{character}' in the string is: {string.count(character)}")
  