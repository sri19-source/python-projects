#type conversion
# Type conversion is the process of converting one data type into another.
number=7
number=str(number)  # converting integer to string
print(number)  # '7'

number=float(number)  # converting string to float
print(number)  # 7.0

number=complex(number)  # converting float to complex
print(number)  # (7+0j)

number=int(number.real)  # converting complex to integer
print(number)  # 7

number=bool(number)  # converting integer to boolean
print(number)  # True

