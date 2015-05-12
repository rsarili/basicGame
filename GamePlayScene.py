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
			
		### Create Monsters ###
		self.__monster_group = pygame.sprite.RenderPlain()
		for gameObject in self.__level.getMonsters():
			self.__monster = self.__object_factory.create(self.__monster_group, gameObject[0], gameObject[1], gameObject[2])
			
		self.__scoreboard = ScoreBoard(self.__screen, (5,5), self.__player)
		
		
	def update(self):
		### Move monster ###
		for monster in self.__monster_group:
			monster.do_move()

		### Detect and Handle Collisions ###
		
		### Player and Bomb ###
		self.__bomb_collision_list = pygame.sprite.groupcollide(self.__player_group, self.__bomb_group, False, False)
		for player, bombs in self.__bomb_collision_list.iteritems():
			for bomb in bombs:
				player.collide_bomb(bomb)

		### Player and Explosion ###
		self.__explosion_collision_list = pygame.sprite.groupcollide(self.__player_group, self.__explosion_group, False, False)
		for player, explosions in self.__explosion_collision_list.iteritems():
			for explosion in explosions:
				player.collide_explosion(explosion)
		
		### Player and Powerup ###
		self.__powerups_collision_list = pygame.sprite.groupcollide(self.__player_group, self.__powerups_group, False, True)
		for player, powerups in self.__powerups_collision_list.iteritems():
			for powerup in powerups:
				powerup.effect(player)
			
		### Player and Wall ###
		self.__wall_collision_list = pygame.sprite.groupcollide(self.__player_group, self.__wall_group, False, False)
		for player, walls in self.__wall_collision_list.iteritems():
			for wall in walls:
				player.collide_wall(wall)
			
		### Player and Monster ###
		self.__monster_collision_list = pygame.sprite.groupcollide(self.__player_group, self.__monster_group, False, False)
		for player, monsters in self.__monster_collision_list.iteritems():
			for monster in monsters:
				player.collide_monster(monster)
				monster.collide_player(player)
			
		### Monster and Explosion ###
		self.__monster_collision_list = pygame.sprite.groupcollide(self.__monster_group, self.__explosion_group, False, False)
		for monster, explosion in self.__monster_collision_list.iteritems():
			monster.collide_explosion(explosion)

		### Monster and Wall ###
		self.__monster_collision_list = pygame.sprite.groupcollide(self.__monster_group, self.__wall_group, False, False)
		for monster, walls in self.__monster_collision_list.iteritems():
			for wall in walls:
				monster.collide_wall(wall)
			
		### Wall and Explosion ###
		for wall in pygame.sprite.groupcollide(self.__explosion_group, self.__wall_group, False, False).values():
			self.__wall_group.remove(wall)
		####################################
		
		### Update Groups ###
		self.__player_group.update()
		self.__bomb_group.update()
		self.__explosion_group.update()
		self.__wall_group.update()
		self.__powerups_group.update()
		self.__monster_group.update()
		#####################
		self.__scoreboard.update()
		
	def draw(self):
		#print "GamePlayScene.draw()"
		self.__powerups_group.draw(self.__screen)
		self.__wall_group.draw(self.__screen)
		self.__player_group.draw(self.__screen)
		self.__bomb_group.draw(self.__screen)
		self.__explosion_group.draw(self.__screen)
		self.__monster_group.draw(self.__screen)
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

