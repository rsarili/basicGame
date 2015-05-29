import pygame
from Constants import *
from GameObject import GameObject
from Behaviours import *

### There should be also a non destructable Wall
class Wall(GameObject):
	def __init__(self, pos_x, pos_y):
		GameObject.__init__(self)
		self.__explosion_collision = DieBehaviour()

		self.sprite_sheet = SpriteSheet('wall.png')
		self.worth = 10
		self.image=self.sprite_sheet.get_image(0,0,50,50)
		self.rect=self.image.get_rect()
		self.rect.x = pos_x
		self.rect.y = pos_y
	def collide_explosion(self, explosion):
		self.__explosion_collision.resolve(self, explosion)
