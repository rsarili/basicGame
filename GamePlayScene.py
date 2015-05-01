import pygame
from Scene import Scene
from GameObjectFactory import *
from ScoreBoard import *

class GamePlayScene(Scene):
	def __init__(self, game):
		self.__game = game
		self.bomb = None
		self.__screen = game.getScreen()
		pygame.mouse.set_visible(0)
		self.__level = game.getLevel()
		self.__object_factory = GameObjectFactory()
		
		### Create Players ###
		self.__player_group = pygame.sprite.RenderPlain()
		for gameObject in self.__level.getPlayers():
			self.__player = self.__object_factory.create(self.__player_group, gameObject[0], gameObject[1], gameObject[2])
			
		self.__bomb_group = pygame.sprite.RenderPlain()
				
		### Create Walls ###
		self.__wall_group = pygame.sprite.RenderPlain()
		for gameObject in self.__level.getWalls():
			self.__object_factory.create(self.__wall_group, gameObject[0], gameObject[1], gameObject[2])
		
		self.__explosion_group = pygame.sprite.RenderPlain()
		
		### Create PowerUps ###
		self.__powerups_group = pygame.sprite.RenderPlain()
		for gameObject in self.__level.getPowerups():
			self.__object_factory.create(self.__powerups_group, gameObject[0], gameObject[1], gameObject[2])
			
		self.__scoreboard = ScoreBoard(self.__screen, (5,5), self.__player)
		
		
	def update(self):
		### Detect and Handle Collisions ###
		self.__bomb_collision_list = pygame.sprite.spritecollide(self.__player, self.__bomb_group, False)
		for bomb in self.__bomb_collision_list:
			self.__player.collide_bomb(bomb)

		self.__explosion_collision_list = pygame.sprite.spritecollide(self.__player, self.__explosion_group, False)
		for explosion in self.__explosion_collision_list:
			self.__player.collide_explosion(explosion)
			
		self.__powerups_collision_list = pygame.sprite.spritecollide(self.__player, self.__powerups_group, True)
		for powerup in self.__powerups_collision_list:
			powerup.effect(self.__player)
			
		self.__wall_collision_list = pygame.sprite.spritecollide(self.__player, self.__wall_group, False)
		for wall in self.__wall_collision_list:
			self.__player.collide_wall(wall)
		
		for wall in pygame.sprite.groupcollide(self.__explosion_group, self.__wall_group, False, False).values():
			self.__wall_group.remove(wall)
		####################################
		
		### Update Groups ###
		self.__player_group.update()
		self.__bomb_group.update()
		self.__explosion_group.update()
		self.__wall_group.update()
		self.__powerups_group.update()
		#####################
		self.__scoreboard.update()
		
	def draw(self):
		#print "GamePlayScene.draw()"
		self.__powerups_group.draw(self.__screen)
		self.__wall_group.draw(self.__screen)
		self.__player_group.draw(self.__screen)
		self.__bomb_group.draw(self.__screen)
		self.__explosion_group.draw(self.__screen)
		self.__scoreboard.draw()
		
	def handleEvents(self, events):
		for event in events:
			print "GamePlayScene.handleEvent()"
			if event.type == pygame.QUIT: # If user clicked close
				self.__game.finish()
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					self.__player.stop_vertical()
					self.__player.move_left()
				elif event.key == pygame.K_RIGHT:
					self.__player.stop_vertical()
					self.__player.move_right()
				elif event.key == pygame.K_UP:
					self.__player.stop_horizontal()
					self.__player.move_up()
				elif event.key == pygame.K_DOWN:
					self.__player.stop_horizontal()
					self.__player.move_down()


			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT and self.__player.change_x < 0:
					self.__player.stop_horizontal()
				elif event.key == pygame.K_RIGHT and self.__player.change_x > 0:
					self.__player.stop_horizontal()
				elif event.key == pygame.K_UP and self.__player.change_y < 0:
					self.__player.stop_vertical()
				elif event.key == pygame.K_DOWN and self.__player.change_y > 0:
					self.__player.stop_vertical()
				if event.key == pygame.K_SPACE:
					if(not self.bomb):
						self.bomb = self.__player.drop_bomb()
						self.bomb.register_to_group(self.__bomb_group)
				if event.key == pygame.K_a:
					if(self.bomb):
						self.explodes = self.bomb.explode()
						self.bomb = None
						for explode in self.explodes:
							explode.register_to_group(self.__explosion_group)

