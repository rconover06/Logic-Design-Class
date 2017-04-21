#Raul Conover

import turtle

def draw_multicolor_square(t, sz):
    """Make turtle t draw a multi-color square of sz"""
    for i in ["red","purple","hotpink","blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)

# Create the screen
wn = turtle.Screen()
wn.bgcolor("lightgreen")

# Create the turtle
tess = turtle.Turtle()
tess.pensize(3)
tess.speed(10)

#Set size of smallest square
size = 20

for i in range(50):
    draw_multicolor_square(tess, size)
    size = size + 10        # Increase the size for the next square
    tess.forward(10)        # Move tess along a little
    tess.right(18)          # Rotate the turtle a little

wn.mainloop()
