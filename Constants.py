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
