import pygame
from Constants import *
from GameObject import GameObject
from Behaviours import *

class Monster(GameObject):
	sprite_group = None
	def __init__(self, pos_x, pos_y):
		GameObject.__init__(self)
		self.__explosion_collision = DieBehaviour()
		self.__bomb_collision = DontPassThroughBehaviour()
		self.__wall_collision = DontPassThroughBehaviour()
		self.__player_collision = DontPassThroughBehaviour()
		self.movement_behaviour = None

		self.sprite_sheet = SpriteSheet('avatar_scaled2.png')
		self.frames_left = []
		self.frames_right = []
		self.frames_up = []
		self.frames_down = []
		self.width = 62
		self.height = 62
		self.worth = 100
		###### left frames ###############
		image=self.sprite_sheet.get_image(0,62,self.width,self.height)
		self.frames_left.append(image)
		self.image=image
		image=self.sprite_sheet.get_image(62,62,self.width,self.height)
		self.frames_left.append(image)
		image=self.sprite_sheet.get_image(124,62,self.width,self.height)		
		self.frames_left.append(image)
		image=self.sprite_sheet.get_image(186,62,self.width,self.height)		
		self.frames_left.append(image)
		
		##### right frames ################
		image=self.sprite_sheet.get_image(0,124,self.width,self.height)		
		self.frames_right.append(image)
		image=self.sprite_sheet.get_image(62,124,self.width,self.height)		
		self.frames_right.append(image)
		image=self.sprite_sheet.get_image(124,124,self.width,self.height)		
		self.frames_right.append(image)
		image=self.sprite_sheet.get_image(186,124,self.width,self.height)		
		self.frames_right.append(image)
		
		##### up frames #################
		image=self.sprite_sheet.get_image(0,186,self.width,self.height)		
		self.frames_up.append(image)
		image=self.sprite_sheet.get_image(62,186,self.width,self.height)		
		self.frames_up.append(image)
		image=self.sprite_sheet.get_image(124,186,self.width,self.height)		
		self.frames_up.append(image)
		image=self.sprite_sheet.get_image(186,186,self.width,self.height)		
		self.frames_up.append(image)
		
		##### down frames ###############
		image=self.sprite_sheet.get_image(0,0,self.width,self.height)		
		self.frames_down.append(image)
		image=self.sprite_sheet.get_image(62,0,self.width,self.height)		
		self.frames_down.append(image)
		image=self.sprite_sheet.get_image(124,0,self.width,self.height)		
		self.frames_down.append(image)
		image=self.sprite_sheet.get_image(186,0,self.width,self.height)		
		self.frames_down.append(image)
		##################################
		
		self.rect=self.image.get_rect()
		self.rect.x = pos_x
		self.rect.y = pos_y
		self.change_x = 0
		self.change_y = 0
		self.frame=0
		self.delay=4
		self.pause=0
		self.direction="R"
		self.speed = 3
		self.score = 0
		self.obstacle_position = None

	def load_frames(self):
		image=self.sprite_sheet.get_image(0,192,144,192)
		self.frames_left.append(image)
		self.image=image
		image=self.sprite_sheet.get_image(0,384,144,192)
		self.frames_left.append(image)
		image=self.sprite_sheet.get_image(0,576,144,192)
		self.frames_left.append(image)
		image=self.sprite_sheet.get_image(0,768,144,192)
		self.frames_left.append(image)
		
	def update(self):
		#self.stop_vertical()
		#self.move_right()
		self.rect.x += self.change_x
		self.rect.y += self.change_y
		self.pause += 1
		if self.pause > self.delay:
			self.pause = 0
			if self.direction == "L":
				self.frame = (self.frame + 1) % len(self.frames_left)
				self.image = self.frames_left[self.frame]
			elif self.direction == "R":
				self.frame = (self.frame + 1) % len(self.frames_right)
				self.image = self.frames_right[self.frame]
			elif self.direction == "U":
				self.frame = (self.frame + 1) % len(self.frames_up)
				self.image = self.frames_up[self.frame]
			elif self.direction == "D":
				self.frame = (self.frame + 1) % len(self.frames_down)
				self.image = self.frames_down[self.frame]
				
	def move_left(self):
		self.change_x = -self.speed
	def move_right(self):
		self.change_x = self.speed
	def move_up(self):
		self.change_y = -self.speed
	def move_down(self):
		self.change_y = self.speed
	def move(self):
		if self.direction == "L":
			self.move_left()
		elif self.direction == "R":
			self.move_right()
		elif self.direction == "U":
			self.move_up()
		elif self.direction == "D":
			self.move_down()
	def stop_vertical(self):
		self.change_y = 0
		self.direction = None
	def stop_horizontal(self):
		self.change_x = 0
		self.direction = None
	def collide_bomb(self, bomb):
		self.__bomb_collision.resolve(self, bomb)
	def collide_explosion(self, explosion):
		self.__explosion_collision.resolve(self, explosion)
	def collide_wall(self, wall):
		self.__wall_collision.resolve(self, wall)
	def collide_player(self, player):
		self.__player_collision.resolve(self, player)
	def setSpeed(self, speed):
		self.speed = speed
	def set_collide_wall_behaviour(self, behaviour):
		self.__wall_collision = behaviour
	def do_move(self):
		self.movement_behaviour.move(self)
