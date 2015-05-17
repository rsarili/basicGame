import pygame
from Constants import *
from GameObject import GameObject
from Bomb import Bomb
from Explosion import *

from Behaviours import *

class Player(GameObject):
	sprite_group = None
	def __init__(self, pos_x, pos_y):
		GameObject.__init__(self)
		self.__explosion_collision = DieBehaviour()
		self.__bomb_collision = DontPassThroughBehaviour()
		self.__wall_collision = DontPassThroughBehaviour()
		self.__monster_collision = DontPassThroughBehaviour()
		
		self.sprite_sheet = SpriteSheet('avatar_scaled2.png')
		self.frames_left = []
		self.frames_right = []
		self.frames_up = []
		self.frames_down = []
		self.width = 62
		self.height = 62
		
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
		self.direction=None
		self.speed = 3
		self.score = 0
		self.player_number = 1
		self.bomb_count = 0
		self.bomb_limit = 2
		self.bombs = []

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
				
	def drop_bomb(self):
		self.score += 5
		return Bomb(self.rect.x+5, self.rect.y+5)
		
	def move_left(self):
		self.change_x = -self.speed
		self.direction = "L"
		
	def move_right(self):
		self.change_x = self.speed
		self.direction = "R"
	def move_up(self):
		self.change_y = -self.speed
		self.direction = "U"
		
	def move_down(self):
		self.change_y = self.speed
		self.direction = "D"
		
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
		
	def collide_monster(self, monster):
		self.__monster_collision.resolve(self, monster)
	def setSpeed(self, speed):
		self.speed = speed
		
	def set_collide_wall_behaviour(self, behaviour):
		self.__wall_collision = behaviour
		
	def get_score(self):
		return self.score
		
	def handle_left_pressed(self):
		self.stop_vertical()
		self.move_left()
		
	def handle_right_pressed(self):
		self.stop_vertical()
		self.move_right()
		
	def handle_up_pressed(self):
		self.stop_horizontal()
		self.move_up()
		
	def handle_down_pressed(self):
		self.stop_horizontal()
		self.move_down()
		
	def handle_bomb_dropped_released(self):
		if(self.bomb_count < self.bomb_limit):
			bomb = self.drop_bomb()
			bomb.register_to_group(Bomb.sprite_group)
			self.bomb_count += 1
			self.bombs.append(bomb)
	
	def handle_bomb_explode_released(self):
		if self.bomb_count > 0:
			for bomb in self.bombs:
				explodes = bomb.explode()
				for explode in explodes:
					print("explosion")
					explode.register_to_group(Explosion.sprite_group)
			self.bomb_count = 0
			self.bombs = []
		
	def set_keys_for_player_num(self, player_num):
		if player_num == 1:
			self.__left_key = PLAYER1_LEFT
			self.__right_key = PLAYER1_RIGHT
			self.__up_key = PLAYER1_UP
			self.__down_key = PLAYER1_DOWN
			self.__bomb_drop_key = PLAYER1_BOMB_DROP
			self.__bomb_explode_key = PLAYER1_BOMB_EXPLODE
		elif player_num == 2:
			self.__left_key = PLAYER2_LEFT
			self.__right_key = PLAYER2_RIGHT
			self.__up_key = PLAYER2_UP
			self.__down_key = PLAYER2_DOWN
			self.__bomb_drop_key = PLAYER2_BOMB_DROP
			self.__bomb_explode_key = PLAYER2_BOMB_EXPLODE

	def handle_key_down(self, key):
		if key == self.__left_key:
			self.handle_left_pressed()
		elif key == self.__right_key:
			self.handle_right_pressed()
		elif key == self.__up_key:
			self.handle_up_pressed()
		elif key == self.__down_key:
			self.handle_down_pressed()
	def handle_key_up(self, key):
		if key == self.__left_key and self.change_x < 0:
			self.stop_horizontal()
		elif key == self.__right_key and self.change_x > 0:
			self.stop_horizontal()
		elif key == self.__up_key and self.change_y < 0:
			self.stop_vertical()
		elif key == self.__down_key and self.change_y > 0:
			self.stop_vertical()
		elif key == self.__bomb_drop_key:
			self.handle_bomb_dropped_released()
		elif key == self.__bomb_explode_key:
			self.handle_bomb_explode_released()
			
			
