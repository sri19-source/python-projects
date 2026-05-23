#gst calculation
amount = float(input("Enter the amount: ")) 
gst_rate = float(input("Enter the GST rate (in percentage): "))
gst_amount = (amount * gst_rate) / 100
total_amount = amount + gst_amount
print(f"GST Amount: {gst_amount:.2f}")
print(f"Total Amount (including GST): {total_amount:.2f}")