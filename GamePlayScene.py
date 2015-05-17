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
		self.__players = []
		self.__player_count = 1
		
		### Create Players ###
		self.__player_group = pygame.sprite.RenderPlain()
		for gameObject in self.__level.getPlayers():
			self.__player = self.__object_factory.create(self.__player_group, gameObject[0], gameObject[1], gameObject[2])
			self.__player.set_keys_for_player_num(self.__player_count)
			self.__player_count += 1
			self.__players.append(self.__player)
			
		self.__bomb_group = pygame.sprite.RenderPlain()
		Bomb.sprite_group = self.__bomb_group
				
		### Create Walls ###
		self.__wall_group = pygame.sprite.RenderPlain()
		for gameObject in self.__level.getWalls():
			self.__object_factory.create(self.__wall_group, gameObject[0], gameObject[1], gameObject[2])
		
		self.__explosion_group = pygame.sprite.RenderPlain()
		Explosion.sprite_group = self.__explosion_group
		
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
				for player in self.__players:
					player.handle_key_down(event.key)

			if event.type == pygame.KEYUP:
				for player in self.__players:
					player.handle_key_up(event.key)
