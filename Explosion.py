import pygame
from Constants import *
from GameObject import GameObject
from threading import Timer

class Explosion(GameObject):
	def __init__(self, pos_x, pos_y):
		GameObject.__init__(self)
		self.sprite_sheet = SpriteSheet('bomberman.png')
		image=self.sprite_sheet.get_image(519,1,16,16)
		self.image=image
		self.rect=self.image.get_rect()
		self.rect.x = pos_x
		self.rect.y = pos_y
		
		t =Timer(1.0, lambda:self.deregister_from_group())
		t.start()
