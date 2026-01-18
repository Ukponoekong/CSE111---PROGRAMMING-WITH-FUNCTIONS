"""
Activity: Calling Functions

Purpose
Check your understanding of calling built-in Python functions 
and functions that are in a standard Python module.

Problem Statement
In our modern world economy, many items are manufactured in large 
factories, then packed in boxes and shipped to distribution centers and 
retail stores. A common question for employees who pack items is “How 
many boxes do we need?" 
"""
import math

items = int(input("\nWhat is the number of manufactured items? "))

items_per_box =int(input("What is the number of items to be packed per box? "))

boxes = items / items_per_box

boxes = math.ceil(boxes)

print(f"For {items} items, packing {items_per_box} items in each box, you will need {boxes} boxes.")
print()