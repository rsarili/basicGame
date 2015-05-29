import pygame
from MenuScene import MenuScene
from Level import *
from Constants import *

class Bomberman:
	def __init__(self):
		print("Bomberman")
		self.__screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		pygame.display.set_caption('Bomberman')
		self.__clock = pygame.time.Clock()
		pygame.init()
		pygame.mixer.pre_init()
		#song = pygame.mixer.Sound("JustLikeThat.wav")
		#pygame.mixer.Sound.play(song,-1)
	def start(self):
		print("Height: " + str(SCREEN_HEIGHT))
		print("Width: " + str(SCREEN_WIDTH))
		#self.__current_level.createLevel()
		self.__current_scene = MenuScene(self)
		self.players = []
		while 1:
			self.__clock.tick(60)
			self.__screen.fill(BLACK)
			
			self.__current_scene.handleEvents(pygame.event.get())            
			self.__current_scene.update()
			self.__current_scene.draw()
			
			pygame.display.flip()
	def finish(self):
		exit()
	def setLevel(self, level):
		if(level):
			self.__current_level = level
			self.__current_level.createLevel()
	def getLevel(self):
		return self.__current_level
	def getScreen(self):
		return self.__screen
	def changeScene(self, scene):
		self.__current_scene = scene
	def getWinner(self):
		if self.players[0].isDead:
			return self.players[1]
		else:
			return self.players[0]
	def getLoser(self):
		if self.players[0].isDead:
			return self.players[0]
		else:
			return self.players[1]
		
if __name__ == "__main__":
	game = Bomberman()
	game.start()
