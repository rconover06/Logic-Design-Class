# Raul Conover
# Nested conditionals

import math

x = int(input("Enter a value for x: "))

# Various if and else statements to demonstrate how some of these work

if x % 2 == 0:
    print(x, " is even.")
    print("Did you know 2 is the only even prime number")
else:
    print(x, " is odd.")
    print("Did you know multiplying two odd numbers give an odd result?")

# if statement but with out an else statement
if x < 0:
    print("The negative number", x, " is not valid here.")
    x = 42
    print(" I've decided to use 43 instead.")

print("The square root the absolute value of ", x, " is", math.sqrt(x))
print(" ")

# Using the variable y from now on.

y = int(input("Enter a value for y: "))

# This is a nested if statement.
if 0 < y:
    if y < 10:
        print("y is a positive single digit")
# Same as above nested if statement but only uses 1.
if 0 < y and y < 10:
    print("y is a positive single digit")

# Demonstrate the return statement. Return goes to the caller.
def print_square_root(y):
    if y <= 0:
        print("Positive numbers only please")
        return
    result =  x**0.5
    print("The square root of ", y," is", result)
