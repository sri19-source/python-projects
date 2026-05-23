#dictionary
# A dictionary is a collection of key-value pairs.
# Each key is unique and maps to a value.
# Dictionaries are mutable, meaning you can change them after creation.
# Example of creating a dictionary
student = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
student["hobby"]="badminton"
student["age"]=56
print(student)
print(student.get("city"))
print(student.get("hobby")) #normally get helps to avoid KeyError if the key does not exist
print(student.get("country", "key not found"))  # returns default value if key is not found
print(student.get("city","lasya"))

student1 = {
    "name": "Alice",
    "age": 30,
    "age": "New York"
}
print(student1)# now the compiler consider's the last assigned value for the key

del student1["age"]  # deletes the key-value pair with key "age"