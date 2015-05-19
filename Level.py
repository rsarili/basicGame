from Player import Player
from Wall import *
from PowerUp import *
from Monster import *

class Level:
	def __init__(self):
		self.walls = []
		self.player = []
		self.powerups = []
		self.monsters = []
	def createLevel(self):
		pass
	def getWalls(self):
		return self.walls
	def getPlayers(self):
		return self.player
	def getMonsters(self):
		return self.monsters
	def getPowerups(self):
		return self.powerups

class Level_1_SinglePlayer(Level):
	def __init__(self):
		Level.__init__(self)
		self.createLevel()
	def createLevel(self):
		self.player.append(("Player",200, 100))

		self.walls.append(("Wall", 300, 200))
		self.walls.append(("Wall", 300, 250))
		self.walls.append(("Wall", 300, 300))
		self.walls.append(("Wall", 300, 350))
		self.walls.append(("Wall", 300, 400))
		
		self.powerups.append(("PhaseMod", 400, 400))
		self.powerups.append(("SpeedUp", 500, 500))
		
		self.monsters.append(("Monster",100, 300))
		self.monsters.append(("Monster",100, 400))
		self.monsters.append(("Monster",100, 500))
		print("Level 1 Single Player is created")
		
class Level_1_MultiPlayer(Level):
	def __init__(self):
		Level.__init__(self)
		self.createLevel()
	def createLevel(self):
		self.player.append(("Player",100, 100))
		self.player.append(("Player",200, 100))

		self.walls.append(("Wall", 300, 200))
		self.walls.append(("Wall", 300, 250))
		self.walls.append(("Wall", 300, 300))
		self.walls.append(("Wall", 300, 350))
		self.walls.append(("Wall", 300, 400))
		
		self.powerups.append(("PhaseMod", 400, 400))
		self.powerups.append(("SpeedUp", 500, 500))
		
		self.monsters.append(("Monster",100, 300))
		self.monsters.append(("Monster",100, 400))
		self.monsters.append(("Monster",100, 500))
		print("Level 1 Multi Player is created")
		
		

	
