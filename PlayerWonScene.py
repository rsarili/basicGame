from Scene import *
from Constants import *

class Text():
	def __init__(self, pos, text, font):
		self.__pos = pos
		self.__text = text
		self.__font = font
		self.__item = self.__font.render(self.__text, True, RED)

	def draw(self, screen):
		self.__item = self.__font.render(self.__text, True, RED)
		screen.blit(self.__item,self.__pos)
	
class PlayerWonScene(Scene):
	def __init__(self, game):
		self.__game = game
		self.__screen = game.getScreen()
		self.__font_big=pygame.font.SysFont(None,75)
		self.__font_little=pygame.font.SysFont(None,50)

		
		self.__game_over_text = Text((220,100),"Player X Win", self.__font_big)
		self.__score_text = Text((220,200),"Player 1 Score: "+ str(self.__game.players[0].score), self.__font_little)
	def update(self):
		pass
	def draw(self):
		self.__game_over_text.draw(self.__screen)
		self.__score_text.draw(self.__screen)
	def handleEvents(self, event):
		pass

