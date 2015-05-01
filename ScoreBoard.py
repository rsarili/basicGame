import pygame
import time
import math
from Constants import *

class ScoreBoard:
		def __init__(self,screen, pos, player):
			self.screen = screen
			self.font = pygame.font.SysFont(None,30)
			self.pos = pos
			self.player = player
			self.time_new = self.time_prev = time.time()
			self.time = 0
		def update(self):
			self.time += math.trunc( math.floor(self.time_new) - math.floor(self.time_prev))
			self.text_score = "SCORE: " + str(self.player.get_score())
			self.text_time = "Time : " + str(self.time)
			self.time_prev = self.time_new
			self.time_new = time.time()
			
		def draw(self):
			self.item_score = self.font.render(self.text_score, True, BLUE)
			self.item_time = self.font.render(self.text_time, True, BLUE)
			self.screen.blit(self.item_score, self.pos)
			self.screen.blit(self.item_time, (self.pos[0], self.pos[1]+40))
