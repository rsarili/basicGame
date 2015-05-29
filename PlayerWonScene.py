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
		self.__font_big=pygame.font.SysFont(None,60)
		self.__font_little=pygame.font.SysFont(None,50)
		winner = self.__game.getWinner()
		loser = self.__game.getLoser()
		
		self.__winner_text = Text((120,100), winner.get_name() + " Won" +" Score: " + str(winner.get_score()), self.__font_big)
		self.__loser_text = Text((120,200),"Loser is "+loser.get_name()+ " Score: " + str(loser.get_score()), self.__font_little)
		
	def update(self):
		pass
	def draw(self):
		self.__winner_text.draw(self.__screen)
		self.__loser_text.draw(self.__screen)
	def handleEvents(self, event):
		pass
