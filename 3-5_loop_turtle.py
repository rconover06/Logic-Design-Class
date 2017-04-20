#Raul Conover


# Import Stuff
import sys
sys.path.insert(0,'c:\Python34\Lib')
import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("3.5 For Loops with Turtles")

# Create a turtle named Alex
alex = turtle.Turtle()

for i in [0,1,2,3,4]:
    alex.forward(50)
    alex.left(90)

wn.mainloop()
    
