x = 3
y = 6

comparsion=None
match True:
    case _ if x > y:
        print("x is greater than y")
    case _ if x < y:
        print("x is less than y")
    case _ if x == y:
        print("x is equal to y")
    case _:
        print("Invalid comparison")
