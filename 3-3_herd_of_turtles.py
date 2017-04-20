# Raul Conover

import turtle

# Setup window and its atributes
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Tess and Alex")

# Create Tess and set attributes
tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(5)

# Create Alex
alex = turtle.Turtle()

# Make tess draw tringle
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)

# tess turns around
tess.right(180)
tess.forward(80)

# Make alex draw a square
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.mainloop()
