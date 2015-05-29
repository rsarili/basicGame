import pygame
from Scene import Scene
from GameObjectFactory import *
from ScoreBoard import *
from Level import *
from GameOverScene import *
from PlayerWonScene import *

class GamePlayScene(Scene):
	def __init__(self, game):
		self.__game = game
		self.bomb = None
		self.__screen = game.getScreen()
		pygame.mouse.set_visible(0)
		self.__level = game.getLevel()
		self.createLevelScene(self.__level)
		
	def createLevelScene(self, level):
		self.__object_factory = GameObjectFactory()
		self.__players = []
		self.__player_count = 1
		
		### Create Players ###
		self.__player_group = pygame.sprite.RenderPlain()
		print("Create Level")
		for gameObject in level.getPlayers():
			self.__player = self.__object_factory.create(self.__player_group, gameObject[0], gameObject[1], gameObject[2])
			self.__player.set_keys_for_player_num(self.__player_count)
			print("Set Keys player count " + str(len(level.getPlayers())))
			self.__player_count += 1
			self.__players.append(self.__player)
		
		### This is a kind of hack to pass players scores to next level ###
		### Because every level players created again ###
		### For first time player creation ###
		if not self.__game.players:
			for i in range(len(self.__players)):
				self.__game.players.append(self.__players[i])
		### Not first time creation
		else:
			for i in range(len(self.__players)):
				self.__players[i].score = self.__game.players[i].score
				self.__game.players[i] = self.__players[i]
		####################################################################
		
		### Create a Empty Bomb group, so created bomb can register ###
		self.__bomb_group = pygame.sprite.RenderPlain()
		Bomb.sprite_group = self.__bomb_group
				
		### Create Walls ###
		self.__wall_group = pygame.sprite.RenderPlain()
		Wall.sprite_group = self.__wall_group
		for gameObject in level.getWalls():
			self.__object_factory.create(self.__wall_group, gameObject[0], gameObject[1], gameObject[2])
		
		self.__explosion_group = pygame.sprite.RenderPlain()
		Explosion.sprite_group = self.__explosion_group
		
		### Create PowerUps ###
		self.__powerups_group = pygame.sprite.RenderPlain()
		for gameObject in level.getPowerups():
			self.__object_factory.create(self.__powerups_group, gameObject[0], gameObject[1], gameObject[2])
			
		### Create Monsters ###
		self.__monster_group = pygame.sprite.RenderPlain()
		Monster.sprite_group = self.__monster_group
		self.monster_list = []
		for gameObject in level.getMonsters():
			self.__monster = self.__object_factory.create(self.__monster_group, gameObject[0], gameObject[1], gameObject[2])
			self.monster_list.append(self.__monster)
		level.setMonsterBehaviours(self.monster_list)
		
		### Create Doors ###
		self.__door_group = pygame.sprite.RenderPlain()
		for gameObject in level.getDoors():
			self.__door = self.__object_factory.create(self.__door_group, gameObject[0], gameObject[1], gameObject[2])
		
		### Create ScoreBoard ###
		self.__scoreboard = ScoreBoard(self.__screen, (5,5), self.__players)
		
	def update(self):
		### Move monster ###
		for monster in self.__monster_group:
			monster.do_move()
			
		### Detect and Handle Collisions ###
		for player in self.__players:
			if player.isDead:
				if len(self.__players) == 1:
					self.__game.changeScene(GameOverScene(self.__game))
				elif len(self.__players) == 2:
					self.__game.changeScene(PlayerWonScene(self.__game))
				
		
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
				player.collide_powerup(powerup)
			
		### Player and Wall ###
		self.__wall_collision_list = pygame.sprite.groupcollide(self.__player_group, self.__wall_group, False, False)
		for player, walls in self.__wall_collision_list.iteritems():
			for wall in walls:
				player.collide_wall(wall)
				
		### Player and Door ###
		self.__door_collision_list = pygame.sprite.groupcollide(self.__player_group, self.__door_group, False, False)
		for player, doors in self.__door_collision_list.iteritems():
			for door in doors:
				self.__game.setLevel(self.__level.getNextLevel())
				self.__level = self.__game.getLevel()
				self.createLevelScene(self.__level)
			
		### Player and Monster ###
		self.__monster_collision_list = pygame.sprite.groupcollide(self.__player_group, self.__monster_group, False, False)
		for player, monsters in self.__monster_collision_list.iteritems():
			for monster in monsters:
				player.collide_monster(monster)
				monster.collide_player(player)
			
		### Monster and Explosion ###
		self.__monster_collision_list = pygame.sprite.groupcollide(self.__monster_group, self.__explosion_group, False, False)
		for monster, explosions in self.__monster_collision_list.iteritems():
			for explosion in explosions:
				monster.collide_explosion(explosion)
			
		### Monster and Bomb ###
		self.__monster_collision_list = pygame.sprite.groupcollide(self.__monster_group, self.__bomb_group, False, False)
		for monster, bombs in self.__monster_collision_list.iteritems():
			for bomb in bombs:
				monster.collide_bomb(bomb)

		### Monster and Wall ###
		self.__monster_collision_list = pygame.sprite.groupcollide(self.__monster_group, self.__wall_group, False, False)
		for monster, walls in self.__monster_collision_list.iteritems():
			for wall in walls:
				monster.collide_wall(wall)
			
		### Wall and Explosion ###
		self.__wall_collision_list = pygame.sprite.groupcollide(self.__wall_group, self.__explosion_group, False, False)
		for wall, explosions in self.__wall_collision_list.iteritems():
			for explosion in explosions:
				wall.collide_explosion(explosion)
		####################################
		
		### Update Groups ###
		self.__player_group.update()
		self.__bomb_group.update()
		self.__explosion_group.update()
		self.__wall_group.update()
		self.__powerups_group.update()
		self.__monster_group.update()
		self.__door_group.update()
		#####################
		self.__scoreboard.update()
		
	def draw(self):
		self.__powerups_group.draw(self.__screen)
		self.__door_group.draw(self.__screen)
		self.__wall_group.draw(self.__screen)
		self.__player_group.draw(self.__screen)
		self.__bomb_group.draw(self.__screen)
		self.__explosion_group.draw(self.__screen)
		self.__monster_group.draw(self.__screen)

		self.__scoreboard.draw()
		
	def handleEvents(self, events):
		for event in events:
			if event.type == pygame.QUIT:
				self.__game.finish()
				
			if event.type == pygame.KEYDOWN:
				for player in self.__players:
					player.handle_key_down(event.key)

			if event.type == pygame.KEYUP:
				for player in self.__players:
					player.handle_key_up(event.key)
