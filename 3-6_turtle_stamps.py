#Raul Conover


# Import Stuff
import sys
sys.path.insert(0,'c:\Python34\Lib')
import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

# Lift the pen up. Does not leave a number
tess.penup()
size = 20

for i in range(30):
    tess.stamp()
    size = size + 3
    tess.forward(size)
    tess.right(24)

wn.mainloop()
