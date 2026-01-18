"""
Author: Ukpono Ekong

W01 Code-along Activity: Discount

Background
You work for a retail store that wants to increase sales on Tuesday 
and Wednesday, which are the store’s slowest sales days. On Tuesday 
and Wednesday, if a customer’s subtotal is $50 or greater, the store
 will discount the customer’s subtotal by 10%
"""

print("\nWelcome to The Famous store!")

quantity = 1

print("\nEnter the quantity and price for each item.")

while quantity != 0:
    try:
        quantity = int(input("\nEnter the quantity? "))
        if quantity == 0:
            break

        price = float(input("Enter the price? "))

        #Get customer's subtotal and use float to convert customers input to string
        subtotal = round(price * quantity, 2)
        subtotal += subtotal

    except ValueError:
        print("Invaid input! Enter an integer or float for the quantities and prices.")

#import Python's built-in datetime module from the standard library 
from datetime import datetime

#Get current date and time
current_time = datetime.now()

#Day of the week by index when Monday=0 to Sunday=6
day_of_week = current_time.weekday()

#Assign index to the days of the week
days = ["Monday", "Tuesday", "Wedneday", "Thursday", "Friday", "Saturday", "Sunday"]

#Use the index to determine the current day of the week from the days in the list
current_day = days[day_of_week]

print(f"Total order: {subtotal:.2f}$")

if subtotal >= 50 and current_day in ["Tuesday", "Wednesday"]:
    percent_subtotal = round(subtotal * (10 / 100), 2)
    discount = round(subtotal - percent_subtotal, 2)

    #Sales tax calculations
    sales_tax = round(discount * (6 / 100), 2)
    total_amount = round(discount + sales_tax, 2)

    print(f"Discount: {percent_subtotal:.2f}$")
    print(f"Sale tax: {sales_tax:.2f}$")
    print(f"Total Due: {total_amount:.2f}$")
    print()

elif current_day in ["Tuesday", "Wednesday"] and subtotal < 50:
    sales_tax = round(subtotal * (6 / 100), 2)
    total_amount = round(subtotal + sales_tax, 2)

    print(f"Sale tax: {sales_tax:.2f}$")
    print(f"Total Due: {total_amount:.2f}$")
    
    qualify_for_discount = 50 - subtotal
    print(f"You would need to purchase extra items worth {qualify_for_discount}$ to receive the discount.")
    print()

else:
    #Sales tax calculations and round() function to round up the sales tax
    sales_tax = round(subtotal * (6 / 100), 2)
    total_amount = round(subtotal + sales_tax, 2)

    print(f"Sale tax: {sales_tax:.2f}$")
    print(f"Total Due: {total_amount:.2f}$")
    print()

    
    


