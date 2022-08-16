#!/usr/bin/python3
# Tip Calculator Day 2 project

print("Welcome to the tip calculator")
bill = input("What was the total bill?")
tip = input("What percentage tip would you like to give? 10, 12, or 15?")
total_people = input("How many people want to split the bill?")
tip_percentage = float(tip) / 100
tip_as_per_bill = float(tip_percentage) * float(bill)
final_bill = float(bill) + float(tip_as_per_bill)
final_bill_per_person = float(final_bill) / int(total_people)
amount_to_pay = round(float(final_bill_per_person), 2)

print(f"Each person should pay: ${amount_to_pay}")
