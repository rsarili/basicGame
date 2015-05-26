from GameObject import *

class CollisionBehaviour():
	def resolve(self, gameObject1, gameObject2):
		pass

class DieBehaviour(CollisionBehaviour):
	def resolve(self, gameObject1, explosion):
		explosion.player.score += gameObject1.worth
		gameObject1.deregister_from_group()
		print "DieBehaviour"
		
class PlayerDieBehaviour(CollisionBehaviour):
	def resolve(self, gameObject1, gameObject2):
		print "PlayerDieBehaviour"
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
			player.obstacle_position = "D"
		elif(player.rect.top >= gameObject.rect.top and player.rect.top < gameObject.rect.bottom and player.direction == "U"):
			player.change_y = 0
			player.rect.top = gameObject.rect.bottom
			player.obstacle_position = "U"
		elif( player.rect.left >= gameObject.rect.left and player.rect.left  <= gameObject.rect.right and player.direction == "L"):
			player.change_x = 0
			player.rect.left = gameObject.rect.right
			player.obstacle_position = "L"
		elif(player.rect.right <= gameObject.rect.right and player.rect.right  >= gameObject.rect.left and player.direction == "R"):
			player.change_x = 0
			player.rect.right = gameObject.rect.left
			player.obstacle_position = "R"

class MovementBehaviour():
	def move(self, monster):
		pass

class RightLeftMovementBehaviour(MovementBehaviour):
	def move(self, monster):
		if monster.obstacle_position == "R":
			monster.direction = "L"
		elif monster.obstacle_position == "L":
			monster.direction = "R"
		monster.move()
		monster.obstacle_position = None
class CircularMovementBehaviour(MovementBehaviour):
	def move(self, monster):
		if monster.obstacle_position == "R":
			monster.direction = "U"
		elif monster.obstacle_position == "U":
			monster.direction = "L"
		elif monster.obstacle_position == "L":
			monster.direction = "D"
		elif monster.obstacle_position == "D":
			monster.direction = "R"
		monster.move()
		monster.obstacle_position = None


