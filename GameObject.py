import pygame

class GameObject(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
	def register_to_group(self, group):
		self.group = group
		self.group.add(self)
	def deregister_from_group(self):
		if(self.group):
			self.group.remove(self)
