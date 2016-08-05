def fixLandscape(minecraft, pos, length, height, blockID):
    minecraft.setBlocks(pos.x-20, pos.y, pos.z-20,
                        pos.x+length+15, pos.y+255, pos.z+length+15, 0)
    minecraft.setBlocks(pos.x-20, pos.y-1, pos.z-20,
                        pos.x+length+15, pos.y-10, pos.z+length+15, blockID)
                        
def buildColumn(minecraft, x, y, z, height, blockID):
    for i in range(height):
        minecraft.setBlock(x, y+i, z, blockID)
    
def buildWalls(minecraft, startPos, length, height, blockID):
    for i in range(length):
        if i % 2 == 0:
            currentHeight = height+1
        else:
            currentHeight = height
        buildColumn(minecraft, startPos.x+i, startPos.y, startPos.z, currentHeight, blockID)
        buildColumn(minecraft, startPos.x, startPos.y, startPos.z+i, currentHeight, blockID)
        buildColumn(minecraft, startPos.x+length-i-1, startPos.y, startPos.z+length-1, currentHeight, blockID)
        buildColumn(minecraft, startPos.x+length-1, startPos.y, startPos.z+length-i-1, currentHeight, blockID)

    offset = (height/2)
    for i in range(length-height):
        buildColumn(minecraft, startPos.x+offset+i, startPos.y, startPos.z+offset, height, blockID)
        buildColumn(minecraft, startPos.x+offset, startPos.y, startPos.z+offset+i, height, blockID)
        buildColumn(minecraft, startPos.x+length-i-offset-1, startPos.y, startPos.z+length-1-offset, currentHeight, blockID)
        buildColumn(minecraft, startPos.x+length-offset-1, startPos.y, startPos.z+length-offset-i-1, currentHeight, blockID)

def buildGate(minecraft, startPos, length, height, blockID):
    offset = height/2
    gateHeight = height*2/3
    middle = length/2
    minecraft.setBlocks(startPos.x, startPos.y, startPos.z+middle-2,
                        startPos.x, startPos.y+gateHeight, startPos.z+middle+1, blockID)
    minecraft.setBlocks(startPos.x+offset, startPos.y, startPos.z+middle-2,
                        startPos.x+offset, startPos.y+gateHeight, startPos.z+middle+1, blockID)

def buildWalkways(minecraft, startPos, length, height, blockID):
    offset = height/2
    minecraft.setBlocks(startPos.x+1, startPos.y+height-1, startPos.z+1,
                        startPos.x+length-2, startPos.y+height-1, startPos.z+offset-1, blockID)
    minecraft.setBlocks(startPos.x+1, startPos.y+height-1, startPos.z+length-2,
                        startPos.x+length-2, startPos.y+height-1, startPos.z+length-offset, blockID)
    minecraft.setBlocks(startPos.x+1, startPos.y+height-1, startPos.z+1,
                        startPos.x+offset-1, startPos.y+height-1, startPos.z+length-2, blockID)
    minecraft.setBlocks(startPos.x+length-2, startPos.y+height-1, startPos.z+1,
                        startPos.x+length-offset, startPos.y+height-1, startPos.z+length-2, blockID)

def buildKeep(minecraft, startPos, length, height, blockID):
    keepHeight = 3 * height
    keepLength = length/3
    wallOffset = height/2
    numFloors = keepHeight // 5
    numWindows = keepLength // 3
    x = startPos.x+length-wallOffset-2
    z = startPos.z+length-wallOffset-2
    minecraft.setBlocks(x, startPos.y, z,
                        x-keepLength, startPos.y+keepHeight, z-keepLength, blockID)
    #hollow out the inside of the keep
    minecraft.setBlocks(x-1, startPos.y, z-1,
                        x-keepLength+1, startPos.y+keepHeight-1, z-keepLength+1, 0)
    #make a space for the door
    minecraft.setBlocks(x-keepLength, startPos.y+1, z-keepLength/2-1,
                        x-keepLength, startPos.y+3, z-keepLength/2+1, 0)
    for i in range(numFloors):
        y = startPos.y + i * 5 + 2
        for j in range(int(numWindows)):
            x2 = x - 2 - 3*j
            z2 = z - 2 - 3*j
            minecraft.setBlocks(x, y, z2,
                                x, y+1, z2, 0)
            minecraft.setBlocks(x-keepLength, y, z2,
                                x-keepLength, y+1, z2, 0)
            minecraft.setBlocks(x2, y, z,
                                x2, y+1, z, 0)
            minecraft.setBlocks(x2, y, z-keepLength,
                                x2, y+1, z-keepLength, 0)

def buildKeepFloors(minecraft, startPos, length, height, blockID):
    keepHeight = 3 * height
    numFloors = keepHeight // 5
    keepLength = length/3
    wallOffset = height/2
    x = startPos.x+length-wallOffset-2
    z = startPos.z+length-wallOffset-2
    for i in range(numFloors):
        y = startPos.y + i*5
        minecraft.setBlocks(x-1, y, z-1,
                            x-keepLength+1, y, z-keepLength+1, blockID)
    
def clean(minecraft, startPos, length, height):
    buildWalls(minecraft, startPos, length, height, 0)
    buildWalkways(minecraft, startPos, length, height, 0)
    buildWalkways(minecraft, startPos, length, height, 0)
    buildKeep(minecraft, startPos, length, height, 0)
    buildKeepFloors(minecraft, startPos, length, height, 0)
    fixLandscape(minecraft, startPos, length, height, 0)

    
