import pygame
from Constants import *
from GameObject import GameObject

class Door(GameObject):
	def __init__(self, pos_x, pos_y):
		GameObject.__init__(self)

		self.sprite_sheet = SpriteSheet('door.png')
		
		self.image=self.sprite_sheet.get_image(0,0,48,50)
		self.rect=self.image.get_rect()
		self.rect.x = pos_x
		self.rect.y = pos_y
