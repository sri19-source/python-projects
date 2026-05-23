#quiz score evaluation
score = 0

print("Simple Quiz")

q1 = input("1. ux full form? ")
if q1.lower() == "user experience":
    score += 1

q2 = input("2. 5 + 3 = ? ")
if q2 == "8":
    score += 1

q3 = input("3. Python is a programming language? (yes/no) ")
if q3.lower() == "yes":
    score += 1

q4 = input("4. AI full form is? ")
if q4.lower() == "artificial intelligence":
    score += 1

q5 = input("5. big data is a part of artificial intelligence? ")
if q5.lower() == "yes":
    score += 1

print("Your score is:", score, "/5")