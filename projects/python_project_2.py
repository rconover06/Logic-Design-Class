# Raul Conover
# Logic Design 1309
# Create a program that is able to guess a number between 0 and 100
# in as few guesses as possible by working off higher or lower clues from user.

# Start Functions
def guess_num(guess,):
    """ Ask if guess is correct, Ifreturn ans
    """
    print("Is your number", guess, "?")
    ans = str(input("[Y/N]:"))
    print()
    if ans == "y" or ans == "yes":
        print("I have guessed your number. It was", guess,".")
        print("It took", count,"attempts to guess it correctly")
    else:
        return ans

def high_low(guess,):
    """ Ask if guess is higher or lower, return hilo
    """
    print("Is your number higher or lower than", guess,"?")
    hilo = str(input("Higher or Lower: "))
    print()
    return hilo

# End Functions

# Set the initial range (high and low), calculate guess, and create counter.
low = -1
high = 101
guess = (high + low) // 2
count = 1

# Setup the rules for the user
print("Write down a number from", low + 1,"and", high - 1,".")
print("If the guess is wrong tell me if your number is higer or lower.")
print("I will try to guess it in as few guesses as possible.")
print()

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
            guess = (high + low) // 2
            count = count + 1
        # else/If the number is lowe set high = guess then calculate newguess. Set newguess = guess.
        # Increase count by 1.
        elif hilo == "l" or hilo == "lower":
            high = guess
            guess = (low + high) // 2
            count = count + 1
    # If the guess is correct end the loop.
    else:
        repeat = False

# Debuging prints to see what variables are when program completes.
#print("ans:", ans)
#print("hilo:", hilo)
#print("count:", count)
#print("low:", low)
#print("high:", high)
#print("guess:", guess)


