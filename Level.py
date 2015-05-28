from Player import Player
from Wall import *
from PowerUp import *
from Monster import *
from Behaviours import *

class Level:
	def __init__(self):
		self.walls = []
		self.player = []
		self.powerups = []
		self.monsters = []
		self.doors = []
		self.next_level = None
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
	def getDoors(self):
		return self.doors
	def getNextLevel(self):
		return self.next_level
	def setMonsterBehaviours(self):
		pass
		

class Level_1_SinglePlayer(Level):
	def __init__(self):
		Level.__init__(self)
		self.next_level = Level_2_SinglePlayer()
		
	def createLevel(self):
		self.player.append(("Player",200, 100))

		self.walls.append(("Wall", 300, 200))
		self.walls.append(("Wall", 300, 250))
		self.walls.append(("Wall", 300, 300))
		self.walls.append(("Wall", 300, 350))
		self.walls.append(("Wall", 300, 400))
		self.walls.append(("Wall", 20, 300))
		self.walls.append(("Wall", 20, 200))

		self.walls.append(("Wall", 20, 400))
		self.walls.append(("Wall", 20, 500))
		self.walls.append(("Wall", 100, 500))

		
		self.powerups.append(("PhaseMod", 400, 400))
		self.powerups.append(("SpeedUp", 500, 500))
		
		self.monsters.append(("Monster",100, 300))
		self.monsters.append(("Monster",100, 400))
		self.monsters.append(("Monster",100, 500))
		
		self.doors.append(("Door",500, 100))


		print("Level 1 Single Player is created")
	def setMonsterBehaviours(self, monsters):
		monsters[0].movement_behaviour = RightLeftMovementBehaviour()
		monsters[1].movement_behaviour = CircularMovementBehaviour()
		monsters[2].movement_behaviour = RightLeftMovementBehaviour()

class Level_2_SinglePlayer(Level):
	def __init__(self):
		Level.__init__(self)
		self.next_level = Level_Finished_SinglePlayer()
		
	def createLevel(self):
		self.player.append(("Player",200, 100))

		self.walls.append(("Wall", 300, 200))
		self.walls.append(("Wall", 300, 250))
		self.walls.append(("Wall", 300, 300))
		self.walls.append(("Wall", 300, 350))
		self.walls.append(("Wall", 300, 400))
		
		self.powerups.append(("PhaseMod", 400, 400))
		self.powerups.append(("PhaseMod", 480, 400))
		self.powerups.append(("PhaseMod", 560, 400))

		self.powerups.append(("SpeedUp", 500, 500))
		
		self.monsters.append(("Monster",100, 300))
		self.monsters.append(("Monster",100, 400))
		self.monsters.append(("Monster",100, 500))
		
		self.doors.append(("Door",500, 100))

		print("Level 2 Single Player is created")
	def setMonsterBehaviours(self, monsters):
		monsters[0].movement_behaviour = RightLeftMovementBehaviour()
		monsters[1].movement_behaviour = RightLeftMovementBehaviour()
		monsters[2].movement_behaviour = RightLeftMovementBehaviour()
		
class Level_Finished_SinglePlayer(Level):
	def __init__(self):
		Level.__init__(self)
	def createLevel(self):
		self.player.append(("Player",200, 100))
	def setMonsterBehaviours(self, monsters):
		pass
		


class Level_1_MultiPlayer(Level):
	def __init__(self):
		Level.__init__(self)
		self.next_level = Level_Empty()
		
	def createLevel(self):
		self.player.append(("Player",100, 100))
		self.player.append(("Player",200, 100))

		self.walls.append(("Wall", 300, 200))
		self.walls.append(("Wall", 300, 250))
		self.walls.append(("Wall", 300, 300))
		self.walls.append(("Wall", 300, 350))
		self.walls.append(("Wall", 300, 400))
		
		self.powerups.append(("PhaseMod", 400, 400))
		self.powerups.append(("PhaseMod", 450, 400))

		self.powerups.append(("SpeedUp", 500, 500))
		
		self.monsters.append(("Monster",100, 300))
		self.monsters.append(("Monster",100, 400))
		self.monsters.append(("Monster",100, 500))
		print("Level 1 Multi Player is created")
	def setMonsterBehaviours(self, monsters):
		monsters[0].movement_behaviour = CircularMovementBehaviour()
		monsters[1].movement_behaviour = CircularMovementBehaviour()
		monsters[2].movement_behaviour = CircularMovementBehaviour()

		
class Level_Empty(Level):
	def __init__(self):
		Level.__init__(self)
	def createLevel(self):
		pass
	def setMonsterBehaviours(self, monsters):
		pass


