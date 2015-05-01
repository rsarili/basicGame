import pygame
from Scene import Scene
from GamePlayScene import GamePlayScene
from MenuScene import MenuScene
from Level import *
from Constants import *
from Player import Player

class Bomberman:
	def __init__(self):
		print("Bomberman")
		self.__screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		pygame.display.set_caption('Bomberman')
		
		self.__clock = pygame.time.Clock()
		self.__current_level = Level_1()
		pygame.init()
		pygame.mixer.pre_init()
		#song = pygame.mixer.Sound("JustLikeThat.wav")
		#pygame.mixer.Sound.play(song,-1)
	def start(self):
		print("Height: " + str(SCREEN_HEIGHT))
		print("Width: " + str(SCREEN_WIDTH))
		self.__current_level.createLevel()
		self.__current_scene = MenuScene(self)
		
		while 1:
			self.__clock.tick(60)
			self.__screen.fill((0, 0, 0))
			
			self.__current_scene.handleEvents(pygame.event.get())            
			self.__current_scene.update()
			self.__current_scene.draw()
			
			pygame.display.flip()
	def finish(self):
		exit()
	def getLevel(self):
		return self.__current_level
	def getScreen(self):
		return self.__screen
	def changeScene(self, scene):
		self.__current_scene = scene
