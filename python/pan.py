#pan card number validation
pan_card_number = input("Enter your PAN card number: ")  
if len(pan_card_number) == 10 and pan_card_number[:5].isalpha() and pan_card_number[5:9].isdigit() and pan_card_number[9].isalpha():
    print("Valid PAN card number.")
else:
    print("Invalid PAN card number.")
