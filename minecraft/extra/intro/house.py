from mcpi.minecraft import Minecraft
from mcpi import block as blocks

mc = Minecraft.create()

def buildColumn(x, y, z, height, block):
    for i in range(height):
        mc.setBlock(x, y+i, z, block)

def buildDoor(x, y, z, height, block):
    door = blocks.DOOR_WOOD.id
    mc.setBlock(x, y+1, z, door)
    #mc.setBlock(x, y+1, z, door)

    extraBlocks = height - 2    #subtract height of door to find extra blocks
##    if extraBlocks > 0:
##        for i in range(extraBlocks):
##            mc.setBlock(x, y+2+i, z, block)
    
def buildWalls(x, y, z):
    woodPlanks = blocks.WOOD_PLANKS.id

    #Build left, right, and back wall
    for i in range(5):
        buildColumn(x+i, y , z, 3, woodPlanks)
        buildColumn(x+i, y, z+5, 3, woodPlanks)
        buildColumn(x+4, y, z+i, 3, woodPlanks)

    #Build front wall, except door.
    for i in range(2):
        buildColumn(x, y, z+i, 3, woodPlanks)
        buildColumn(x, y, z+i+3, 3, woodPlanks)

    buildDoor(x, y, z+2, 3, woodPlanks)

def buildHouse(x, y, z):
    pass

def main():
    mc.postToChat("Hello World!")
    x, y, z = mc.player.getPos()
    buildWalls(x+3, y, z)
if __name__ == "__main__":
    main()
    
