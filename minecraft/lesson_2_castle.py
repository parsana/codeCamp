from mcpi.minecraft import Minecraft
from mcpi import block as blocks
from time import sleep

############### TASK 1 #####################
'''You may remember yesterday, we needed to use the 'turtle' library. Today,
    we need to use the custom library 'castle'. It contains functions that we
    will use to create our castle. Write the line of code that will let us use
    the 'castle' library below. You can look above, or at code from yesterday
    if you cant remember how.'''


############### TASK 2 #####################
''' Open the file, castle.py. Take a quick look at all the 'def *name*():' lines.
    These are called function definitions. Functions allow us to reuse the code
    we write, so we don't have to rewrite it. At the bottom of the castle file,
    add a new function definition called:
    'buildGate(minecraft, startPos, length, height blockID)', we will use it to
    create an opening in our wall so we can actually get inside.'''


############### TASK 3 #####################
''' Once you have created the function definition, lets add some code to actually
    make it do something! Copy the following code into the function 'buildGate'
    in castle.py. Dont uncomment the code here, only in castle.py'''
#    offset = height/2
#    gateHeight = height*2/3
#    middle = length/2
#    minecraft.setBlocks(startPos.x, startPos.y, startPos.z+middle-2,
#                        startPos.x, startPos.y+gateHeight, startPos.z+middle+1, blockID)
#    minecraft.setBlocks(startPos.x+offset, startPos.y, startPos.z+middle-2,
#                        startPos.x+offset, startPos.y+gateHeight, startPos.z+middle+1, blockID)


############### TASK 4 #####################
''' Now that we have all the functions we will need to build our castle, lets start
    getting some of the variables we will need ready. We need to connect to our
    minecraft game like in the first lesson, and get the players position. Finish
    the variable assignment of position. Hint: how did we get player position in the
    last lesson'''
#mc = Minecraft.create()
#mc.postToChat("Let's build a castle!")
#position = 


############### TASK 4 #####################
''' Lets assign some of the blocks we are going to use to build the walls, floors,
    and other things. You can make the blocks whatever youd like, though I'd
    recommend using stone brick for the walls, and wood for walkways and floors.
    try googling 'raspberry pi minecraft block id' to find the block id numbers'''
#walls = 
#floors = 
#grass = 2
#gate = 0

############### TASK 5 #####################
''' Okay, we're ready to start building! I've written the command to flatten the
    ground where our castle will go below. You'll need to write out the rest of
    the functions out. They all take the same'''
#castleHeight = 6
#castleLength = 30
#position.x = position.x+1

#castle.fixLandscape(mc, position, castleLength, castleHeight, grass)

''' The other functions you will need to use are:
    castle.buildWalls(?, ?, ?, ?, ?)
    castle.buildWalkways(?, ?, ?, ?, ?)
    castle.buildGate(?, ?, ?, ?, ?) <-- You added this one!
    castle.buildKeep(?, ?, ?, ?, ?)
    castle.buildKeepFloors(?, ?, ?, ?, ?)
    Add them below!'''


############### TASK 6 #####################
''' We end up with a lot of castles floating around if we dont destroy them. The
    castle library has a 'clean' function that will erase the castle and landscape.
    We should clean up our castle after some time, like a minute. We can use the
    'sleep' function to wait for the give number of seconds before we clean up.'''
#wait = 
#sleep(wait)
#castle.clean(mc, position, castleLength, castleHeight)
