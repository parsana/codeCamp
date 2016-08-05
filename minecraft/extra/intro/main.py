from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

mc = Minecraft.create()

'''mc.postToChat() will send the text into the game for us, and display it
on the screen'''
mc.postToChat("Hello world!")

'''mc.player.getPos() returns your position as an x,y,z coordinate.
Its like saying, From the player in the minecraft game, get their position. '''
pos = mc.player.getPos()

x,y,z = mc.player.getPos()

'''mc.player.setPos(x, y, z) moves the player to the coordinates specified.
Its great for teleporting! '''
#mc.player.setPos(x, y+100, z)

'''mc.setBlock(x, y, z, blockID) creates a block at the specified coordinates.
The blockID is the the type of block you'd like to create.
   1: Smoothstone
   2: Grass
   3: Dirt '''
#mc.setBlock(x+1, y, z, 1)

'''We can use the block import from earlier to refer to blocks by name.
Here we get the wood plank constant, and then get its id. We then create it
a few blocks behind the stone block we created earlier.'''
#mc.setBlock(x+3, y, z, block.WOOD_PLANKS.id)

'''We can use 'variables' to store the id of a block, so we dont have to remember
it later! We can either give it the id directly, or get it from the block constant
Change the code so that it spawns a block of gold instead of a block
of dirt! '''
#dirt = 3
#gold = block.GOLD_BLOCK.id
#mc.setBlock(x+2, y, z, dirt)

'''Some blocks have special properties, like wool. It has many different colors. We can
specify the color to the setBlock function. Wool has the id of 35, set it below. '''
#wool = 35

'''Now to specify the color, we pass in an extra parameter to the setBlock function, after
the block id. Try changing the wools color from white, to one of the colors below!
   1: Orange, 2: Pink, 3: Blue, 4: Yellow '''  
#mc.setBlock(x+4, y, z, wool, 1)

'''We can create lots of blocks using the mc.setBlocks() command, It takes 2 sets of x, y,
z coordinates, and uses them to fill a volume with blocks. We can create a cube of blocks
by making the difference equal on all sides.'''
#stone = 1
#mc.setBlocks(x+5, y+1, z+1, x+15, y+11, z+11, stone)

'''Now we know how to create blocks, but what if we want to do something with them? Lets
start by leaving a trail of flowers behind us wherever we walk. This will involve using a
'while True' loop, which will run forever, or at least until we stop it.'''
#flower = 38
#while True:
'''We need to check the players position every time we loop, so we can put a flower exactly
    where they are standing'''
#    x,y,z = mc.player.getPos()
#    mc.setBlock(x, y, z, flower)
'''We use sleep so the program doesnt try to place a flower as quickly as possible, but waits
    a little bit. A loop with no sleep is called a 'busy loop', it never takes a break!'''
#    sleep(0.1)

'''Since flowers in the sky are a little strange, lets try and make it so we only place a flower
    when the player is walking on grass. We can use mc.getBlock() to get the block at a position.
    We can get the block below the player to see what they are standing on.'''
#x,y,z = mc.player.getPos()
#blockBelow = mc.getBlock(x, y-1, z)
#print(blockBelow)
'''Now, lets put the getBlock() method into a 'while True' loop, and keep printing the block
    below the player.'''
#while True:
#    x, y, z = mc.player.getPos()
#    blockBelow = mc.getBlock(x, y-1, z)
#    print(blockBelow)

''' We can add an if statement to check if the block below us is grass, and if it is, we will
    plant a flower.'''
#grass = 2
#flower = 38
#while True:
#    x, y, z = mc.player.getPos()
#    blockBelow = mc.getBlock(x, y-1, z)
#    print(blockBelow)
#    if blockBelow == grass:
#        mc.setBlock(x, y, z, flower)
#    sleep(0.1)

''' How about we change the block underneath us, so if it isnt grass, we make it grass, and
    put a flower down? We can use an else statement after our if to specify what to do if
    the block isnt grass. So essentially it becomes, if block below is grass, plant flower.
    Else, make block below grass.'''
##grass = 2
##flower = 38
##while True:
##    x, y, z = mc.player.getPos()
##    blockBelow = mc.getBlock(x, y-1, z)
##    print(blockBelow)
##    if blockBelow == grass:
##        mc.setBlock(x, y, z, flower)
##    else:
##        mc.setBlock(x, y, z, grass)
##    sleep(0.1)

''' Lets play with some tnt... we can create tnt using the methods from before, setBlock'''
#tnt = 46
#mc.setBlock(x, y, z, tnt)

''' Try hitting the block with your sword. Huh, nothing happens. Thats no fun. It doesnt
    explode, because it has another property like wool, except it specifies wheter the
    TNT is active or not. Try creating the tnt with additional property 1 that will make it
    explosive!'''
#tnt = 46
#mc.setBlock(x, y, z, tnt, 1)

''' Thats more like it!! But the explosion still wasn't big enough. Why dont we try creating
    a cube of tnt, like how we created a cube of TNT earlier? A big explosion will slow down our
    raspberry pi's... Any bigger than 10x10x10 might crash it!'''
#tnt = 46
#mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, tnt, 1)

'''TNT is pretty fun... What about lava? Its pretty neat too! Its pretty cool, because as it cools
    down, it becomes rock! Lets try creating some now!'''
#lava = 10
#water = 8
#air = 0

#mc.setBlock(x+3, y+3, z, lava)
#sleep(20)
#mc.setBlock(x+3, y+5, z, water)
#sleep(4)
#mc.setBlock(x+3, y+5, z, air)

