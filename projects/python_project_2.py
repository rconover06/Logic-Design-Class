# Raul Conover
# Logic Design 1309
# Create a program that is able to guess a number between 0 and 100
# in as few guesses as possible.

import sys

# Start Functions
def guess_num(guess,):
    """ Ask if guess is correct, return y or n
    """
    print("Is your number", guess, "?")
    ans = str(input("[Y/N]:"))
    if ans == "y" or ans == "yes":
        print("I have guessed your number. It was", guess,".")
    else:
        return ans

def high_low(guess,):
    """ Ask if number x is higher or lower
    """
    print("Is your number higher or lower than", guess,"?")
    hilo = str(input(": "))
    return hilo

# End Functions



# Set the initial range for the program.
low = 0
high = 100
guess = (high + low) // 2


# Setup the rules for the user
print("Write down a number from ", low," to ", high,".",
      "I will try to guess it in as few guesses as possible.")

repeat = True
ans = "y"

while repeat:
    if ans == "y": #or ans == "yes":
        ans = guess_num(guess,)
    else:
        hilo = high_low(guess,)
        if hilo == "h":
            low = guess
            newguess = ((high // 2) + high) // 2
            guess = newguess
            ans = guess_num(guess,)
            newguess = ((high // 2) + high) // 2
            guess =  newguess
            ans = guess_num(guess,)
        else:
            high = guess
            newguess = (low + high) // 2
            guess = newguess
            ans = guess_num(guess,)
        repeat = False

#print("ans:",ans,"hilo:", hilo, "low:", low, "high:", high, "guess:", guess, "newguess:", newguess)


