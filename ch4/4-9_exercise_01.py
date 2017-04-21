# Raul Conover

import turtle

# Create  turtle t draw a square of sz (size)
def d_sq(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

# Create the window
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Ch. 4 Exercise 1")

# Create the turtle
tex = turtle.Turtle()
tex.color("hotpink")
tex.pensize(3)

for i in range(5):
    d_sq(tex, 20)
    tex.penup()
    tex.forward(40)
    tex.pendown()

wn.mainloop()
