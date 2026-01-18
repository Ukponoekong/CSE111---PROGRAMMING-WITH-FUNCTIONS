#After customer's tire volume is calculated, I wrote a program that confirms if the user 
# wants to purchase a tire with the specific volume. If yes the program collects 
# and store the user's name, phone number and volume.

"""
Author: Ukpono Ekong

Week 01 Project: Tire Volume

Overview
This program will accept user input that describes a tire then calculate and 
display the tire's volume. Record the tire information in a log file.

"""

#Import math module from Python standard 
import math

#Import datetime class from the datetime module Python standard datetime library 
from datetime import datetime

# used "\n" to print a line space 
width = int(input("\nEnter the tire width of the tire in mm (ex 205): "))

ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))

diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = math.pi * width**2 * ratio * (width * ratio + 2540 * diameter) / 10000000000

#Round up volume to 2 decimal places.
volume = round(volume, 2)

print(f"The approximate volume is {volume:.2f} liters")

#Get current date and time
current_date_and_time = datetime.now(tz=None)

#Get Year, month, day
current_date = current_date_and_time.date()

#open file with the with() function to ensure file automatically closes

with open("volumes.txt", "at") as volume_file:

    #print the values of this variables to the file named volumes.txt
    print(f"{current_date}, {width}, {ratio}, {diameter}, {volume}", file=volume_file)
    
buy = input("\nDo you want to buy tire with the dimensions you entered? ").lower()

if buy == "yes":
    phone_number = int(input("Enter your phone number?: "))

    buyer_name = input("Enter your name: ").title()

    with open("volumes.txt", "at") as volume_file:

        #print the values of this variables to the file named volumes.txt
        print(f"Customer Name: {buyer_name}, Phone Number: {phone_number}, Tire Volume: {volume}", file=volume_file)
        print("Thank you for your patronage.")
else:
    print("Thank you for your input.")
print()