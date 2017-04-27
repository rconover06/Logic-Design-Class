# Raul Conover
# Logic Design 1309
# Create a program that is able to guess a number between 0 and 100
# in as few guesses as possible.

import sys

# Start Functions
def guess_num(guess,):
    """ Guess a number x and ask yes or no if it is it
    """
    print(" Is your number", guess, "?")
    ans = str(input("[Y/N]:"))
    if ans == "y" or ans == "yes":
        print("I have guessed your number. It was", guess,".")
    else:
        return ans

def high_low(guess,):
    """ Ask if number x is higher or lower
    """
    print("Is your number higher or lower than", guess,"?")
    hilo = str(input(":"))
    return hilo

def min_num(guess, newguess,):
    """ Determine the minium the number can be
    """
    minimum = int(lowest + 0)
    return minimum

def max_num(guess, newguess,):
    """ Determine the max the number can be.
    """
    maximum = int(highest + 0)
    return maximum

# End Functions



# Set the initial range for the program.
lowest = 0
highest = 100
guess = int((highest + lowest) // 2)

minimum = min_num(guess,)
maximum = max_num(guess,)
newguess = (minimum + maximum) //2

# Setup the rules for the user
print("Write down a number from ", lowest," to ", highest,".",
      "I will try to guess it in as few guesses as possible.")

repeat = True
ans = "y"

while repeat:
    if ans == "y": #or ans == "yes":
        ans = guess_num(guess,)
    elif ans =="n": #or ans == "no":
        hilo = high_low(guess,)
        if hilo == "hihger":
            minimum = min_num(guess, newguess,)
            maximum = max_num(guess, newguess,)
            ans = guess_num(guess, newguess)
        else:
            minimum = min_num(guess, newguess,)
            maximum = max_num(guess, newguess,)
            ans == guess_num(int(guess / 2,))
        repeat = False

print("ans:",ans,"hilo:", hilo,", min:", minimum, "max:", maximum, ", guess:", guess)


