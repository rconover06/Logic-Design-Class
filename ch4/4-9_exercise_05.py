# Raul Conover

import turtle

# Create  turtle t draw a square of sz (size)
def d_sq(t, sz):
    for i in range(1):
        t.right(90)
        t.forward(sz)

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

wn = m_win("lightgreen", "4.9 Exercise 4")
tex = m_turt("blue", 2)
tex.speed(10)
leo = m_turt("blue", 2)
leo.speed(10)

size = 3

for i in range(99):
    d_sq(tex, size)
    size = size + 2

leo.penup()
leo.forward(225)
leo.pendown()

size = 3

for i in range(99):
    d_sq(leo, size)
    size = size + 2
    leo.left(1)

wn.mainloop()
