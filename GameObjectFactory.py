from GameObject import *
from Bomb import *
from Explosion import *
from Wall import *
from PowerUp import *
from Player import *
from Monster import *
from Door import *

class GameObjectFactory:
	def create(self, group, gameObject, pos_x, pos_y):
		if(gameObject == "Player"):
			self.gameObject = Player(pos_x, pos_y)
		if(gameObject == "Monster"):
			self.gameObject = Monster(pos_x, pos_y)
		elif(gameObject == "Wall"):
			self.gameObject = Wall(pos_x, pos_y)
		elif(gameObject == "Bomb"):
			self.gameObject =  Bomb(pos_x, pos_y)
		elif(gameObject == "Explosion"):
			self.gameObject = Explosion(pos_x, _pos_y)
		elif(gameObject == "SpeedUp"):
			self.gameObject =  SpeedUp(pos_x, pos_y)
		elif(gameObject == "PhaseMod"):
			self.gameObject =  PhaseMod(pos_x, pos_y)
		elif(gameObject == "Door"):
			self.gameObject = Door(pos_x, pos_y)
		
		self.gameObject.register_to_group(group)
		return self.gameObject
