"""
Python does offer magic methods like sum() and others, please try to write down your algorithms or coding 
instructions clearly without using any shortcuts
"""
# Multiply 3 and any number
def mult(number):
    result = number * 3 #takes argument and multipies by 3 
    print result #prints the result the argument multiplied by 3 
    return result #function returns the result

# adds two numbers together
def add(a, b):
    result = a + b #adds the two arguments together
    print result #prints the result of adding the two arguments together in console
    return result #function returns the result

"""
Using data structures like list, can you find the total or the values in that list.
Do not use a function like sum(someList), that would be cheating ;-)
"""
# Data structure
numbers = [1,2,3,6]

def sumOfListNumbers(someList): 
    total = 0 #sets the total to 0
    for num in someList: #runs a for loop passing in a number from the numbers list each time
        total += num #takes the total and adds the current number selected in the list. 
    print total #prints total after for loop has run through all of the numbers in the list
    return total #returns the total number after running the function


# Program checker (do not change the lines below)
assert sumOfListNumbers(numbers) == 12
assert mult(3) == 9
assert add(1,3) == 4
