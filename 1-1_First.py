# Raul Conover
# This is my first python program 4/13/2017
# I commented out the original operations as we made them more complex.

print("Hello, Python world!")
print("Raul Conover is programming in python.")

# This is to format the z into something readable.
# Add commas and round to 2 decimal places, f is fixed format.
formatstr = ",.2f"

#x = 2
x = float(input("Enter a value for the base:"))
#y = 20
y = float(input("Enter a value for the exponent:"))
z = x**y
#print(z)
# creates new vatiable named answer, formats z using the formatstr we created earlier
answer = format(z,formatstr)
print(x,"raised to the", y, "power =", answer)



