# Raul Conover
# Write a program that draws a star

import turtle

# Create the Screen
wn = turtle.Screen()
wn.title("3.8 Star")

# Create the pen/turtle
star = turtle.Turtle()
star.pensize(2)
star.hideturtle()

# Draw the turtle
for i in range(5):
    star.forward(150)
    star.right(144)

wn.mainloop()
