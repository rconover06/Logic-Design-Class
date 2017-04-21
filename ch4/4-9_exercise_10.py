# Raul Conover

import turtle

# Create  turtle t draw a square of sz (size)
def draw_star(t, sz):
    for i in range(5):
        t.forward(sz)
        t.right(144)

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
tex = m_turt("hotpink", 2)
tex.speed(10)

for i in range(5):
    draw_star(tex, 100)
    tex.penup()
    tex.forward(350)
    tex.right(144)
    tex.pendown()

wn.mainloop()
