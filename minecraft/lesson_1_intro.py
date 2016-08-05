from mcpi.minecraft import Minecraft
from mcpi import block as blocks
from time import sleep

'''Connect to our open minecraft game'''
mc = Minecraft.create()


################ TASK 1 ####################
'''The first thing we should do is figure out how to print out 'Hello World'.
    We cant use the python print statement, we need to use the minecraft functions
    to do so. Change the hello variable to 'Hello World' below.'''
hello = ""
mc.postToChat(hello)


################ TASK 2 ####################
'''To do anything in minecraft, we need to find out where the player is. We can
    do so by using minecrafts 'player.getPos()' function. It returns a variable
    that contains an x, y, and z value. We can access the x/y/z value with
    your_variable.x, your_variable.y, or your_variable.z'''
position = mc.player.getPos()
#mc.postToChat(position)
'''Instead of printing 'What is x?' below, try printing the value of x in the position'''
#mc.postToChat()


################ TASK 3 ####################
'''You can change the players location by using the 'player.setPos(x,y,z)' function.
    Try and teleport the player 100 blocks into the air!'''
#height = 
x = position.x
y = position.y
z = position.z
#mc.player.setPos(x, y+height, z)


################ TASK 4 ####################
'''Now that we know where the player is located, we can place some blocks around
    them! Minecraft provides a setBlock(x, y, z, blockID) function that will create
    a block at x,y,z value you give it.'''
stoneBlock = 1
x = position.x
y = position.y
z = position.z
#mc.setBlock(x, y, z, stoneBlock)
'''You can see that the block is created right where the player is standing. Try
    adding 1 to the x value so it spawns beside the player instead.'''


################ TASK 5 ####################
'''Building block by block can be repetitive... we can use the
    'setBlocks(x,y,z, x2, y2, z2, blockID)' function to create many blocks at once.
    Lets create a 4 x 4 x 4 cube using setBlocks'''
x = position.x + 1
y = position.y
z = position.z
#mc.setBlocks(x, y, z, x+3, y+3, z+3, stoneBlock)
'''Now try to create a much bigger cube, like 10x10x10. Replace the '_' with a number
    to create a 10x10x10 cube.'''
#mc.setBlocks(x, y, z, x+_, y+_, z+_, stoneBlock)

################ TASK 6 ####################




