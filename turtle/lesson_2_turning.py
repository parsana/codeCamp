import turtle               # allows us to use the turtles library


window = turtle.Screen()    # creates a graphics window
bradley = turtle.Turtle()   # create a turtle named bradley
bradley.shape("turtle")     # transform bradley into turtle form

# Exit when you click the turtle graphics window
def exit ():
    window.exitonclick()


#########################################################

# Now let's try making the turtle turn around.
# To do this you need to instruct the turtle not only to move forward,
# but also to turn right or left.

bradley.forward(100)
bradley.right(90)
bradley.forward(100)

# Let's try to draw a square!
# [insert code below]


# Exit the program
exit()
