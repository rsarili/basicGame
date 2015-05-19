from GameObject import *

class CollisionBehaviour():
	def resolve(self, gameObject1, gameObject2):
		pass

class DieBehaviour(CollisionBehaviour):
	def resolve(self, gameObject1, gameObject2):
		print "DieBehaviour"
		
class TakeBehavior(CollisionBehaviour):
	def resolve(self, gameObject1, gameObject2):
		print "TakeBehaviour"
		
class PassThroughBehaviour(CollisionBehaviour):
	def resolve(self, gameObject1, gameObject2):
		print "PassThroughBehaviour"
		
class DontPassThroughBehaviour(CollisionBehaviour):
	def resolve(self, player, gameObject):
		if(player.rect.bottom <= gameObject.rect.bottom and player.rect.bottom > gameObject.rect.top and player.direction == "D"):
			player.change_y = 0
			player.rect.bottom = gameObject.rect.top
		elif(player.rect.top >= gameObject.rect.top and player.rect.top < gameObject.rect.bottom and player.direction == "U"):
			player.change_y = 0
			player.rect.top = gameObject.rect.bottom
		elif( player.rect.left >= gameObject.rect.left and player.rect.left  <= gameObject.rect.right and player.direction == "L"):
			player.change_x = 0
			player.rect.left = gameObject.rect.right
		elif(player.rect.right <= gameObject.rect.right and player.rect.right  >= gameObject.rect.left and player.direction == "R"):
			player.change_x = 0
			player.rect.right = gameObject.rect.left


