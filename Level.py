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
		self.player.append(("Player",80, 50))

		## Top Walls ##
		self.walls.append(("Wall", 0, -20))
		self.walls.append(("Wall", 50, -20))
		self.walls.append(("Wall", 100, -20))
		self.walls.append(("Wall", 150, -20))
		self.walls.append(("Wall", 200, -20))
		self.walls.append(("Wall", 250, -20))
		self.walls.append(("Wall", 300, -20))
		self.walls.append(("Wall", 350, -20))
		self.walls.append(("Wall", 400, -20))
		self.walls.append(("Wall", 450, -20))
		self.walls.append(("Wall", 500, -20))
		self.walls.append(("Wall", 550, -20))
		self.walls.append(("Wall", 600, -20))
		self.walls.append(("Wall", 650, -20))
		self.walls.append(("Wall", 700, -20))
		self.walls.append(("Wall", 750, -20))
		self.walls.append(("Wall", 800, -20))
		
		## Bottom Walls ##
		self.walls.append(("Wall", 0, 580))
		self.walls.append(("Wall", 50, 580))
		self.walls.append(("Wall", 100, 580))
		self.walls.append(("Wall", 150, 580))
		self.walls.append(("Wall", 200, 580))
		self.walls.append(("Wall", 250, 580))
		self.walls.append(("Wall", 300, 580))
		self.walls.append(("Wall", 350, 580))
		self.walls.append(("Wall", 400, 580))
		self.walls.append(("Wall", 450, 580))
		self.walls.append(("Wall", 500, 580))
		self.walls.append(("Wall", 550, 580))
		self.walls.append(("Wall", 600, 580))
		self.walls.append(("Wall", 650, 580))
		self.walls.append(("Wall", 700, 580))
		self.walls.append(("Wall", 750, 580))
		self.walls.append(("Wall", 800, 580))

		## Left Walls ##
		self.walls.append(("Wall", -20, 30))
		self.walls.append(("Wall", -20, 80))
		self.walls.append(("Wall", -20, 130))
		self.walls.append(("Wall", -20, 180))
		self.walls.append(("Wall", -20, 230))
		self.walls.append(("Wall", -20, 280))
		self.walls.append(("Wall", -20, 330))
		self.walls.append(("Wall", -20, 380))
		self.walls.append(("Wall", -20, 430))
		self.walls.append(("Wall", -20, 480))
		self.walls.append(("Wall", -20, 530))
		
		## Right Walls ##
		self.walls.append(("Wall", 770, 30))
		self.walls.append(("Wall", 770, 80))
		self.walls.append(("Wall", 770, 130))
		self.walls.append(("Wall", 770, 180))
		self.walls.append(("Wall", 770, 230))
		self.walls.append(("Wall", 770, 280))
		self.walls.append(("Wall", 770, 330))
		self.walls.append(("Wall", 770, 380))
		self.walls.append(("Wall", 770, 430))
		self.walls.append(("Wall", 770, 480))
		self.walls.append(("Wall", 770, 530))


		self.powerups.append(("SpeedUp", 500, 500))
		
		self.walls.append(("Wall",30 , 140))
		self.walls.append(("Wall",80 , 140))
		self.walls.append(("Wall",130 , 140))
		self.walls.append(("Wall",180 , 140))
		self.walls.append(("Wall",230 , 140))
		self.walls.append(("Wall",280 , 140))
		self.walls.append(("Wall",330 , 140))
		self.walls.append(("Wall",380 , 140))

		self.monsters.append(("Monster",100, 200))
		self.monsters.append(("Monster",100, 300))
		self.monsters.append(("Monster",100, 400))
		
		self.walls.append(("Wall",650 , 20))
		self.walls.append(("Wall",650 , 50))
		self.walls.append(("Wall",650 , 100))
		self.walls.append(("Wall",650 , 150))
		self.walls.append(("Wall",650 , 200))
		self.walls.append(("Wall",650 , 250))
		self.walls.append(("Wall",650 , 300))

		self.doors.append(("Door",700, 100))

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
		
		## Top Walls ##
		self.walls.append(("Wall", 0, -20))
		self.walls.append(("Wall", 50, -20))
		self.walls.append(("Wall", 100, -20))
		self.walls.append(("Wall", 150, -20))
		self.walls.append(("Wall", 200, -20))
		self.walls.append(("Wall", 250, -20))
		self.walls.append(("Wall", 300, -20))
		self.walls.append(("Wall", 350, -20))
		self.walls.append(("Wall", 400, -20))
		self.walls.append(("Wall", 450, -20))
		self.walls.append(("Wall", 500, -20))
		self.walls.append(("Wall", 550, -20))
		self.walls.append(("Wall", 600, -20))
		self.walls.append(("Wall", 650, -20))
		self.walls.append(("Wall", 700, -20))
		self.walls.append(("Wall", 750, -20))
		self.walls.append(("Wall", 800, -20))
		
		## Bottom Walls ##
		self.walls.append(("Wall", 0, 580))
		self.walls.append(("Wall", 50, 580))
		self.walls.append(("Wall", 100, 580))
		self.walls.append(("Wall", 150, 580))
		self.walls.append(("Wall", 200, 580))
		self.walls.append(("Wall", 250, 580))
		self.walls.append(("Wall", 300, 580))
		self.walls.append(("Wall", 350, 580))
		self.walls.append(("Wall", 400, 580))
		self.walls.append(("Wall", 450, 580))
		self.walls.append(("Wall", 500, 580))
		self.walls.append(("Wall", 550, 580))
		self.walls.append(("Wall", 600, 580))
		self.walls.append(("Wall", 650, 580))
		self.walls.append(("Wall", 700, 580))
		self.walls.append(("Wall", 750, 580))
		self.walls.append(("Wall", 800, 580))

		## Left Walls ##
		self.walls.append(("Wall", -20, 30))
		self.walls.append(("Wall", -20, 80))
		self.walls.append(("Wall", -20, 130))
		self.walls.append(("Wall", -20, 180))
		self.walls.append(("Wall", -20, 230))
		self.walls.append(("Wall", -20, 280))
		self.walls.append(("Wall", -20, 330))
		self.walls.append(("Wall", -20, 380))
		self.walls.append(("Wall", -20, 430))
		self.walls.append(("Wall", -20, 480))
		self.walls.append(("Wall", -20, 530))
		
		## Right Walls ##
		self.walls.append(("Wall", 770, 30))
		self.walls.append(("Wall", 770, 80))
		self.walls.append(("Wall", 770, 130))
		self.walls.append(("Wall", 770, 180))
		self.walls.append(("Wall", 770, 230))
		self.walls.append(("Wall", 770, 280))
		self.walls.append(("Wall", 770, 330))
		self.walls.append(("Wall", 770, 380))
		self.walls.append(("Wall", 770, 430))
		self.walls.append(("Wall", 770, 480))
		self.walls.append(("Wall", 770, 530))

		self.walls.append(("Wall", 300, 200))
		self.walls.append(("Wall", 300, 250))
		self.walls.append(("Wall", 300, 300))
		self.walls.append(("Wall", 300, 350))
		self.walls.append(("Wall", 300, 400))
		
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
		## Top Walls ##
		self.walls.append(("Wall", 0, -20))
		self.walls.append(("Wall", 50, -20))
		self.walls.append(("Wall", 100, -20))
		self.walls.append(("Wall", 150, -20))
		self.walls.append(("Wall", 200, -20))
		self.walls.append(("Wall", 250, -20))
		self.walls.append(("Wall", 300, -20))
		self.walls.append(("Wall", 350, -20))
		self.walls.append(("Wall", 400, -20))
		self.walls.append(("Wall", 450, -20))
		self.walls.append(("Wall", 500, -20))
		self.walls.append(("Wall", 550, -20))
		self.walls.append(("Wall", 600, -20))
		self.walls.append(("Wall", 650, -20))
		self.walls.append(("Wall", 700, -20))
		self.walls.append(("Wall", 750, -20))
		self.walls.append(("Wall", 800, -20))
		
		## Bottom Walls ##
		self.walls.append(("Wall", 0, 580))
		self.walls.append(("Wall", 50, 580))
		self.walls.append(("Wall", 100, 580))
		self.walls.append(("Wall", 150, 580))
		self.walls.append(("Wall", 200, 580))
		self.walls.append(("Wall", 250, 580))
		self.walls.append(("Wall", 300, 580))
		self.walls.append(("Wall", 350, 580))
		self.walls.append(("Wall", 400, 580))
		self.walls.append(("Wall", 450, 580))
		self.walls.append(("Wall", 500, 580))
		self.walls.append(("Wall", 550, 580))
		self.walls.append(("Wall", 600, 580))
		self.walls.append(("Wall", 650, 580))
		self.walls.append(("Wall", 700, 580))
		self.walls.append(("Wall", 750, 580))
		self.walls.append(("Wall", 800, 580))

		## Left Walls ##
		self.walls.append(("Wall", -20, 30))
		self.walls.append(("Wall", -20, 80))
		self.walls.append(("Wall", -20, 130))
		self.walls.append(("Wall", -20, 180))
		self.walls.append(("Wall", -20, 230))
		self.walls.append(("Wall", -20, 280))
		self.walls.append(("Wall", -20, 330))
		self.walls.append(("Wall", -20, 380))
		self.walls.append(("Wall", -20, 430))
		self.walls.append(("Wall", -20, 480))
		self.walls.append(("Wall", -20, 530))
		
		## Right Walls ##
		self.walls.append(("Wall", 770, 30))
		self.walls.append(("Wall", 770, 80))
		self.walls.append(("Wall", 770, 130))
		self.walls.append(("Wall", 770, 180))
		self.walls.append(("Wall", 770, 230))
		self.walls.append(("Wall", 770, 280))
		self.walls.append(("Wall", 770, 330))
		self.walls.append(("Wall", 770, 380))
		self.walls.append(("Wall", 770, 430))
		self.walls.append(("Wall", 770, 480))
		self.walls.append(("Wall", 770, 530))

		self.walls.append(("Wall", 300, 200))
		self.walls.append(("Wall", 300, 250))
		self.walls.append(("Wall", 300, 300))
		self.walls.append(("Wall", 300, 350))
		self.walls.append(("Wall", 300, 400))

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


