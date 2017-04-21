#Raul Conover

import turtle

def draw_square(t, sz):
    """Make turtle t draw a square of sz"""
    for i in range (4):
        t.forward(sz)
        t.left(90)

# Create the window with attributes
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("3.1 Alex meets a function")

alex =  turtle.Turtle()
draw_square(alex, 50)

wn.mainloop()
