from mcpi.minecraft import Minecraft

def houseBuilder(x, y, z):
	 for i in range(0, 10):
	 	mc.setBlock(x +i, y, z)
def main():
	mc = Minecraft.create()
	pos = mc.player.getTilePos()
	houseBuilder(pos.x, pos.y, pos.z)

