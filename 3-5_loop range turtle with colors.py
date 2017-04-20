#Raul Conover


# Import Stuff
import sys
sys.path.insert(0,'c:\Python34\Lib')
import turtle

# Create the screen with attributes
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("3.5 For Loops Using Range")

# Create a turtle named alex with various attributes
alex = turtle.Turtle()
#alex.color("blue")
alex.pensize(3)
alex.shape("turtle")

# Create a turtle named tess with various attributes
tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)
tess.shape("turtle")

# alex draws a shape
clrs_1 = ["yellow","red","purple","blue"]
for c in clrs_1:
    alex.color(c)
    alex.forward(100)
    alex.left(90)
    
# tess draws a triangle
for i in range(3):
    tess.forward(-100)
    tess.right(-120)

# Keeps window open for user to close
wn.mainloop()
    
