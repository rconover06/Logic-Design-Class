# Raul Conover

import turtle

xs = [48, 117, 200, 240, 160, 260, 220]

# Get turtle t to draw one bar of height
def draw_bar(t, height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(' '+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)
    t.pendown()

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("5.12 Bar Graphs with turtles")

tess = turtle.Turtle()
tess.pensize(3)
tess.color("blue", "lightblue")

for v in xs:
    draw_bar(tess, v)

wn.mainloop()
