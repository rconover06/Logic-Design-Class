# Raul Conover

import turtle

# Create  turtle t draw a square of sz (size)
def d_sq(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

# Create the window function
def m_win(color, ttle):
    w = turtle.Screen()
    w.bgcolor(color)
    w.title(ttle)
    return w

# Create funciton to create turtles
def m_turt(colr, size):
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(size)
    return t

wn = m_win("lightgreen", "4.9 Exercise 2")
tex = m_turt("hotpink", 3)

size = 20

for i in range(6):
    d_sq(tex, size)
    tex.right(135)
    tex.penup()
    tex.forward(15)
    tex.left(135)
    size = size + 20
    tex.pendown()

wn.mainloop()
