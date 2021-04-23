print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill?\n$"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15?\n"))
total_bill+= (tip/100) * total_bill
person = int(input("How may people to split the bill?\n"))
bill_paid_by_each = total_bill / person
print(f"Each person should pay:\n${round(bill_paid_by_each, 2)}")