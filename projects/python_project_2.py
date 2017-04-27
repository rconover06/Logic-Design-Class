# Raul Conover
# Logic Design 1309
# Create a program that is able to guess a number between 0 and 1000 in as few guesses as possible.

# Start Functions
def guess_num(x,):
    """ Guess a number x and ask yes or no if it is it
    """
    print(" Is your number", x, "?")
    ans = str(input("[Y/N]:"))
    return ans

#def high_low(g,):
#    """
#    """

# End Functions

x = 500
ans = guess_num(x,)
print(x, ans)

