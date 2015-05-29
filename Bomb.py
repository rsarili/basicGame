import pygame
from Constants import *
from GameObject import GameObject
from Explosion import Explosion
from threading import Timer
from Monster import *
from Wall import *

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
		self.player = player
		self.space_between_explosions_in_px = 15
		self.power = 4
		self.right_explosion_allowed = True
		self.left_explosion_allowed = True
		self.up_explosion_allowed = True
		self.down_explosion_allowed = True

		#t =Timer(5.0, lambda:self.explode())
		#t.start()
	def explode(self):
		self.__explosions = []
		
		for i in range(self.power):
			if self.right_explosion_allowed:
				right_explosion = Explosion(self.rect.x+27+ self.space_between_explosions_in_px * i, self.rect.y+12, self.player)
				right_explosion.register_to_group(Explosion.sprite_group)
				self.__monster_collision_list = pygame.sprite.spritecollide(right_explosion, Monster.sprite_group, False)
				for monster in self.__monster_collision_list:
					self.right_explosion_allowed = False
				
				self.__wall_collision_list = pygame.sprite.spritecollide(right_explosion, Wall.sprite_group, False)
				for wall in self.__wall_collision_list:
					self.right_explosion_allowed = False

			if self.left_explosion_allowed:
				left_explosion = Explosion(self.rect.x+27- self.space_between_explosions_in_px * i, self.rect.y+12, self.player)
				left_explosion.register_to_group(Explosion.sprite_group)
				self.__monster_collision_list = pygame.sprite.spritecollide(left_explosion, Monster.sprite_group, False)
				for monster in self.__monster_collision_list:
					self.left_explosion_allowed = False
				
				self.__wall_collision_list = pygame.sprite.spritecollide(left_explosion, Wall.sprite_group, False)
				for wall in self.__wall_collision_list:
					self.left_explosion_allowed = False
					
			if self.up_explosion_allowed:
				up_explosion = Explosion(self.rect.x+27, self.rect.y+12-self.space_between_explosions_in_px * i, self.player)
				up_explosion.register_to_group(Explosion.sprite_group)
				self.__monster_collision_list = pygame.sprite.spritecollide(up_explosion, Monster.sprite_group, False)
				for monster in self.__monster_collision_list:
					self.up_explosion_allowed = False
				
				self.__wall_collision_list = pygame.sprite.spritecollide(up_explosion, Wall.sprite_group, False)
				for wall in self.__wall_collision_list:
					self.up_explosion_allowed = False
					
			if self.down_explosion_allowed:
				down_explosion = Explosion(self.rect.x+27, self.rect.y+12+self.space_between_explosions_in_px * i, self.player)
				down_explosion.register_to_group(Explosion.sprite_group)
				self.__monster_collision_list = pygame.sprite.spritecollide(down_explosion, Monster.sprite_group, False)
				for monster in self.__monster_collision_list:
					self.down_explosion_allowed = False
				
				self.__wall_collision_list = pygame.sprite.spritecollide(down_explosion, Wall.sprite_group, False)
				for wall in self.__wall_collision_list:
					self.down_explosion_allowed = False
		
		boom = pygame.mixer.Sound("explosion1.ogg")
		pygame.mixer.Sound.play(boom)
		self.deregister_from_group()
