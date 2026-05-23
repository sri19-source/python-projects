#electricity bill calculator
current=int(input("Enter the current meter reading: "))
previous=int(input("Enter the previous meter reading: "))
units=current-previous
def calculate_bill(units):
    if units >=100: 
        bill=100*rate1
    if units >100 and units <=200:
        bill=100*rate1+(units-100)*rate2
    if units >200 and units <=250:
        bill=100*rate1+100*rate2+(units-200)*rate3
    if units >250:
            bill=100*rate1+100*rate2+50*rate3+(units-250)*rate4
    return bill

rate1=0.5
rate2=0.75  
rate3=1.20
rate4=1.50
bill_amount=calculate_bill(units)
print("The electricity bill amount is:", bill_amount)
