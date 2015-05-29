import pygame
from Constants import *
from GameObject import GameObject
from Behaviours import *

class PowerUp(GameObject):
	sprite_group = None
	def __init__(self):
		GameObject.__init__(self)
	def effect(self):
		pass
		
# Other power up can be added like increase bomb range, bomb limit, pass throgh bomb etc...
# Related fields exist in gameObjects. Only need to a power up to change them.

class SpeedUp(PowerUp):
	def __init__(self, pos_x, pos_y):
		PowerUp.__init__(self)
		self.sprite_sheet = SpriteSheet('speedup.png')
		self.image=self.sprite_sheet.get_image(0,0,35,35)
		self.rect=self.image.get_rect()
		self.rect.x = pos_x
		self.rect.y = pos_y
		
	def effect(self, player):
		print("SpeedUp Effect!!!")
		player.setSpeed(10)
		
class PhaseMod(PowerUp):
	def __init__(self, pos_x, pos_y):
		PowerUp.__init__(self)
		self.sprite_sheet = SpriteSheet('phasemod.png')
		self.image=self.sprite_sheet.get_image(0,0,35,35)
		self.rect=self.image.get_rect()
		self.rect.x = pos_x
		self.rect.y = pos_y
		
	def effect(self, player):
		print("PhaseMod Effect!!!")
		player.set_collide_wall_behaviour(PassThroughBehaviour())
