# Raul Conover
# Python Programming Project 1
# Write a program to find total investment using compound interest.

# Format add commas and round to 2 decimal places, f is fixed format.
formatans = ",.2f"

# p = principal(user input)
# r = annual interest rate (user input)
# n = number of times interest is compounded per year(user input)
# t = number of years (user input)
# a = accumulated amount

p = float(input("Enter the principal amount:"))
r = float(input("Enter the annual nominal interest rate:"))
n = int(input("Enter the number of times Interest is compounded per year:"))
t = int(input("Enter the number of years:"))


# A=P(1+(r/n))^nt
a = p*(1+(r/n))**(n*t)
# Formatted soltion for A
ans = format(a,formatans)

print("$",ans)
# if the number of years is greater than 10 display a message. Otherwise just print the total
if(t >= 10):
    print("Long term investments are important for retirement planning.")
