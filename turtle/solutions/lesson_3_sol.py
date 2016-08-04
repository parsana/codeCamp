import turtle

window = turtle.Screen()    # creates a graphics window
bradley = turtle.Turtle()   # create a turtle named bradley
bradley.shape("turtle")     # transform bradley into turtle form
window.colormode(255)       # set color mode

# Exit when you click the turtle graphics window
def exit ():
    window.exitonclick()


##################################################################
# The default colour for the pen used by the turtle cursor is black,
# and the default background colour is white. You can change the colours
# to make your shapes look even better.

# The code below contains three variables called R, G, and B.

R = 255
G = 255
B = 0

window.bgcolor(R, G, B)

# Variables are a way of storing a value and giving it a name.
# For instance, there is a variable name R with a value of 255.
# Try changing the values of the three variables, and see what happens.
# (Note: the maximum value is 255, and after this there will be no effect.)


# Turtles can change color too!
# Declare 3 variables and use the color() function to change Bradley's color
# [insert code below]

A = 100
B = 255
C = 50

bradley.color(A, B, C)

bradley.forward(100)
bradley.right(90)
bradley.forward(100)
bradley.right(90)
bradley.forward(100)
bradley.right(90)
bradley.forward(100)



exit()
