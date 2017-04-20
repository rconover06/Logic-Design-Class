# Raul Conover
# Exercise 3.8 use turtles to create a clock face

import sys
sys.path.insert(0,'c:\Python34\Lib')
import turtle

# Create the screen
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("3.8 Turtle Clock")

#create the turtle
tex = turtle.Turtle()
tex.color("blue")
tex.pensize(3)
tex.shape("turtle")
#tex.speed(5)
tex.hideturtle()

tex.penup()
tex.stamp()
tex.forward(-15)
tex.pendown()
tex.forward(-10)
tex.penup()
tex.stamp()
tex.forward(-100)
tex.stamp()

for i in range(1):
    tex.forward(100)
    tex.pendown()
    tex.forward(10)
    tex.penup()
    tex.forward(15)
    tex.stamp()
    tex.forward(-100)

wn.mainloop()
