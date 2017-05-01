# Raul Conover
# Logic Design 1309
# Create a program that is able to guess a number between 0 and 100
# in as few guesses as possible.

# Start Functions
def guess_num(guess,):
    """ Ask if guess is correct, return ans
    """
    print("Is your number", guess, "?")
    ans = str(input("[Y/N]:"))
    if ans == "y" or ans == "yes":
        print("I have guessed your number. It was", guess,".",
              "It took", count,"attempts to guess it correctly")
#        repeat = False
    else:
        return ans

def high_low(guess,):
    """ Ask if guess is higher or lower, return hilo
    """
    print("Is your number higher or lower than", guess,"?")
    hilo = str(input(": "))
    return hilo

# End Functions

# Set the initial range for the program.
low = 0
high = 100
guess = (high + low) // 2
newguess = guess
hilo = "n"
count = 1

# Setup the rules for the user
print("Write down a number between", low,"to", high,".",
      "I will try to guess it in as few guesses as possible.")

repeat = True

# While repat is True.  Ask the user if guess is thir number.
while repeat:
    ans = guess_num(guess,)
    # if the answer is no or n ask user if their number is higher or lower.
    if ans == "n" or ans == "no":
        hilo = high_low(guess,)
        # If the number is higher set low = guess then calculate newguess. Set newguess = guess.
        # Increase count by 1.
        if hilo == "h" or hilo == "higher":
            low = guess
            newguess = (high + low) // 2
            guess = newguess
            count = count + 1
        # else/If the number is lowe set high = guess then calculate newguess. Set newguess = guess.
        # Increase count by 1.
        elif hilo == "l" or hilo == "lower":
            high = guess
            newguess = (low + high) // 2
            guess = newguess
            count = count + 1
    # If the guess is correct end the loop.
    else:
        repeat = False

# Debuging print to see what numbers are when they complete
#print("ans:",ans,"hilo:", hilo, "low:", low, "high:", high, "guess:", guess, "newguess:", newguess)


