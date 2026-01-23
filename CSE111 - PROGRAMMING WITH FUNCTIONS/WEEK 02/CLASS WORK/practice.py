#Practicing functions from writing simple codes.

def add_intergers(first, second):
    """
    Add the second number and retirn the result
    """
    result = first + second
    return result

#Getting the varaible to be used as parameters from the users
first = int(input("\nEnter an interger "))
second = int(input("Enter an interger "))

#Call the function and assign a name to it
answer = add_intergers(first, second)
print(f"Answer: {answer}")
print()

