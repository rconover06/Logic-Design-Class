# Raul Conover

import turtle
wn = turtle.Screen()
wn.bgcolor(str(input("Enter a background color:")))    # Set window background color
wn.title("Hello, Tess!")    # Set the window title

tess = turtle.Turtle()
tess.color(str(input("Enter a pen color:")))          # Tell tess to change color
tess.pensize(int(input("Enter a pen width:")))             # Tell tess to set her pen width

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.mainloop()
