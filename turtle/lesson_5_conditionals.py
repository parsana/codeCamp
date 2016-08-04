# -*- coding: utf-8 -*-
import turtle

window = turtle.Screen()    # creates a graphics window
bradley = turtle.Turtle()   # create a turtle named bradley
bradley.shape("turtle")     # transform bradley into turtle form
window.colormode(255)       # set color mode

# Exit when you click the turtle graphics window
def exit ():
    window.exitonclick()

###################################################################

# The if-then statement is the most basic of all the control flow statements.
# It tells your program to execute a certain section of code only if
# a particular test evaluates to true.

# if (a condition evaluates to True):
#       then do these things only for ‘True’
# else:
#       otherwise do these things only for ‘False’.


direction = raw_input("Go left or right? ")

if direction == "left":
    bradley.left(60)
    bradley.forward(50)
    exit()
if direction == "right":
    bradley.right(60)
    bradley.forward(50)
    exit()
    
#################################################################

# Let's try coding an if statment to either draw a square or a triangle

shape = raw_input("square or triangle? ")
    












