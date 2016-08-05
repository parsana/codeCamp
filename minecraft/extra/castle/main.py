from mcpi.minecraft import Minecraft
from mcpi import block as blocks
import castle
from time import sleep

#Connect to our minecraft game.
mc = Minecraft.create()

mc.postToChat("Let's build a castle")

pos = mc.player.getPos()


#castle.buildColumn(mc, pos.x+3, pos.y, pos.z, 10, blocks.STONE.id)
castle.fixLandscape(mc, pos, 30, 6, blocks.GRASS.id)
castle.buildWalls(mc, pos, 30, 6, blocks.STONE.id)
castle.buildWalkways(mc, pos, 30, 6, blocks.WOOD_PLANKS.id)
castle.buildGate(mc, pos, 30, 6, blocks.WOOD_PLANKS.id)
castle.buildKeep(mc, pos, 30, 6, blocks.STONE.id)
castle.buildKeepFloors(mc, pos, 30, 6, blocks.WOOD_PLANKS.id)
sleep(30)
castle.clean(mc, pos, 30, 6)
