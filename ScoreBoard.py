import pygame
import time
import math
from Constants import *

class ScoreBoard:
		def __init__(self,screen, pos, players):
			self.screen = screen
			self.font = pygame.font.SysFont(None,30)
			self.pos = pos
			self.players = players
			self.time_new = self.time_prev = time.time()
			self.time = 0
			self.score_texts = [None] * len(self.players)
		def update(self):
			self.time += math.trunc( math.floor(self.time_new) - math.floor(self.time_prev))
			self.text_time = "Time : " + str(self.time)
			self.time_prev = self.time_new
			self.time_new = time.time()
			
			for i in range(len(self.players)):
				text = self.players[i].get_name() + " :"+ str(self.players[i].get_score())
				self.score_texts[i]=text
				
		def draw(self):
			for i in range(len(self.players)):
				self.item_score = self.font.render(self.score_texts[i], True, BLUE)
				self.screen.blit(self.item_score, (self.pos[0]+150*(i+1), self.pos[1]))
			
			self.item_time = self.font.render(self.text_time, True, BLUE)
			self.screen.blit(self.item_time, self.pos)

