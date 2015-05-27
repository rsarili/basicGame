import pygame
from Constants import *
from GameObject import GameObject
from threading import Timer

class Explosion(GameObject):
	sprite_group = None
	image = None
	def __init__(self, pos_x, pos_y, player):
		GameObject.__init__(self)
		if(Explosion.image == None):
			self.sprite_sheet = SpriteSheet('bomberman.png')
			Explosion.image=self.sprite_sheet.get_image(519,1,16,16)
		self.image=Explosion.image
		self.rect=self.image.get_rect()
		self.rect.x = pos_x
		self.rect.y = pos_y
		self.player = player
		t =Timer(1.0, lambda:self.deregister_from_group())
		t.start()
