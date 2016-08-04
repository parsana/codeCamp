import turtle

window = turtle.Screen()    # creates a graphics window
bradley = turtle.Turtle()   # create a turtle named bradley
bradley.shape("turtle")     # transform bradley into turtle form
window.colormode(255)       # set color mode

# Exit when you click the turtle graphics window
def exit ():
    window.exitonclick()
    
###################################################################

# Repeating lines of code is one of the fastest ways to get something done.
# Quite often in computer science, it makes more sense to repeat lines of
# code rather than write out another set of instructions.
# For example, the square you created earlier uses the same two
# instructions four times. Rather than writing them out four times,
# you could write them out once but add an instruction to repeat them.

# In Python there are two types of loops that you are likely to use:
# a while loop and a for loop. If you want a section of code to repeat
# forever, or until a condition is set, then a while loop might be best.
# If you want to loop for a set number of times, then a for loop is preferable.

###################################################################

# Here, we have used a while True loop. This means that the code inside the loop
# (i.e. the code which is indented) will repeat forever.

#while True:
#  bradley.forward(1)
#  bradley.right(1)


###################################################################

# In this example, a for loop has been used. Press Run to see what happens.

#for i in range(8):
#  bradley.write(i)
#  bradley.forward(20)

# A for loop repeats instructions a set number of times, in this case 8 times.
# A for loop has an associated variable (called i here). In this example, i starts
# from 0 and increases by 1 each time.

# for i in range(4):
#  bradley.forward(100)
#  bradley.right(90)


###################################################################

# Once you have created one shape using a loop, you can repeat the shape again
# and again by putting it inside another loop. This is a great way to draw spirals.

# A spiral can be made by turning a small degree and then
# moving forward a small amount. The section of code for making a square is
# inside another for loop that repeats it 30 times, each time turning
# the cursor 25 degress to make a pleasing spiral shape.

#for i in range(30):
#  for i in range(4):
#      bradley.forward(100)
#      bradley.right(90)
#  bradley.right(25)



##################################################################

# Can you alter the for loop so that it draws a more interesting spiral using
# one of the shapes you made earlier, like a triangle?

# Adding a few extra lines where you alter the variables R, G, and B would
# allow you to make a multicoloured spiral. Have a go at creating a rainbow spiral.

# Triangle
for i in range(3):
    bradley.forward(320)
    bradley.left(120)


exit()












