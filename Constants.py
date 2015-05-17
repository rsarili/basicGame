import pygame

#Screen dimensions
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600

# Colors
BLACK    = (   0,   0,   0) 
WHITE    = ( 255, 255, 255) 
BLUE     = (   0,   0, 255)


# class to load images from sprite sheets
class SpriteSheet(object):
	sprite_sheet = None
	def __init__(self, file_name):
		self.sprite_sheet = pygame.image.load(file_name).convert()
	def get_image(self, x, y, width, height):
		image = pygame.Surface([width, height]).convert()
		image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
		image.set_colorkey(BLACK)
		return image


PLAYER1_LEFT = pygame.K_LEFT
PLAYER1_RIGHT = pygame.K_RIGHT
PLAYER1_UP = pygame.K_UP
PLAYER1_DOWN = pygame.K_DOWN
PLAYER1_BOMB_DROP = pygame.K_o
PLAYER1_BOMB_EXPLODE = pygame.K_p

PLAYER2_LEFT = pygame.K_a
PLAYER2_RIGHT = pygame.K_d
PLAYER2_UP = pygame.K_w
PLAYER2_DOWN = pygame.K_s
PLAYER2_BOMB_DROP = pygame.K_SPACE
PLAYER2_BOMB_EXPLODE = pygame.K_e
