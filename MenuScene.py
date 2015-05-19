import pygame
from Constants import *
from Scene import Scene
from GamePlayScene import GamePlayScene
from Level import *

class MenuItem:
	def __init__(self, pos, text, font):
		self.__pos = pos
		self.__hovered = False
		self.__text = text
		self.__font = font
		
		self.__item = self.__font.render(self.__text, True, self.getColor())
		self.__rect = self.__item.get_rect()
		self.__rect.topleft = pos
	def getColor(self):
		if self.__hovered:
			return BLUE
		else:
			return WHITE
	def draw(self, screen):
		self.__item = self.__font.render(self.__text, True, self.getColor())
		screen.blit(self.__item,self.__pos)
	def getRect(self):
		return self.__rect
	def setHover(self, hovered):
		self.__hovered = hovered

class MenuScene(Scene):
	def __init__(self, game):
		self.__game = game
		self.__screen = game.getScreen()
		self.__font=pygame.font.SysFont(None,50)
		
		self.__item1 = MenuItem((60,60),"Single Player", self.__font)
		self.__item2 = MenuItem((60,130),"Two Player", self.__font)
		self.__item3 = MenuItem((60,200),"Exit", self.__font)
		
	def update(self):
		if self.__item1.getRect().collidepoint(pygame.mouse.get_pos()):
			self.__item1.setHover(True)
		else:
			self.__item1.setHover(False)

		if self.__item2.getRect().collidepoint(pygame.mouse.get_pos()):
			self.__item2.setHover(True)
		else:
			self.__item2.setHover(False)
			
		if self.__item3.getRect().collidepoint(pygame.mouse.get_pos()):
			self.__item3.setHover(True)
		else:
			self.__item3.setHover(False)
			
	def draw(self):
		self.__item1.draw(self.__screen)
		self.__item2.draw(self.__screen)
		self.__item3.draw(self.__screen)

	def handleEvents(self, events):
		for event in events:
			if event.type == pygame.MOUSEBUTTONUP:
				print("Single Player")
				if self.__item1.getRect().collidepoint(pygame.mouse.get_pos()):
					self.__game.setLevel(Level_1_SinglePlayer())
					self.__game.changeScene(GamePlayScene(self.__game))
				if self.__item2.getRect().collidepoint(pygame.mouse.get_pos()):
					self.__game.setLevel(Level_1_MultiPlayer())
					self.__game.changeScene(GamePlayScene(self.__game))
