# Raul Conover

# 4.7 Turtles REvisited

import turtle

# Setup the window with given background, color, and title.
# Returns the new window
def make_window(color, ttle):
    w = turtle.Screen()
    w.bgcolor(color)
    w.title(ttle)
    return w

# Setup a turtle with the given colorm and size.
# Returns the new turtle
def make_turtle(colr, sz):
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t

wn = make_window("lightgreen", "Tess and Alex Dancing")
tess = make_turtle("hotpink", 5)
alex = make_turtle("black", 1)
dave = make_turtle("yellow", 2)

alex.forward(100)
tess.forward(-100)
dave.right(90)
dave.forward(100)

wn.mainloop()
