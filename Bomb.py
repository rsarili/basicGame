import pygame
from Constants import *
from GameObject import GameObject
from Explosion import Explosion
from threading import Timer

class Bomb(GameObject):
	sprite_group = None
	def __init__(self, pos_x, pos_y, player):
		GameObject.__init__(self)
		self.sprite_sheet = SpriteSheet('bomb.png')
		image=self.sprite_sheet.get_image(0,0,48,48)
		self.image=image
		self.rect=self.image.get_rect()
		self.rect.x = pos_x
		self.rect.y = pos_y
		self.center_x = self.rect.x + self.rect.width / 2
		self.center_y = self.rect.y + self.rect.height / 2
		print "Called"
		self.player = player
		#t =Timer(5.0, lambda:self.explode())
		#t.start()
	def explode(self):
		print("BOOOM!!!")
		#self.__explosions = []
		#self.__explosions.append()
		
		#self.__explosions.append(Explosion(self.rect.x+27, self.rect.y+12))
		#self.__explosions.append(Explosion(self.rect.x+42, self.rect.y+12))
		#self.__explosions.append(Explosion(self.rect.x-3, self.rect.y+12))
		#self.__explosions.append(Explosion(self.rect.x-18, self.rect.y+12))
		
		#self.__explosions.append(Explosion(self.rect.x+12, self.rect.y+27))
		#self.__explosions.append(Explosion(self.rect.x+12, self.rect.y+42))
		#self.__explosions.append(Explosion(self.rect.x+12, self.rect.y-3))
		#self.__explosions.append(Explosion(self.rect.x+12, self.rect.y-18))
		
		explosion = Explosion(self.center_x, self.center_y, self.player)
		explosion.register_to_group(Explosion.sprite_group)
		
		boom = pygame.mixer.Sound("explosion1.ogg")
		pygame.mixer.Sound.play(boom)
		self.deregister_from_group()

		return explosion
	def xxx(self):
		print("BOOOM!!!")
