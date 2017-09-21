# Liwei Jiang, Yin Li, Kebing Li
# CS269 JP17
# Computer Game Design
# Card.py
# Jan. 15th 2017

import pygame

class Card:

	def __init__(self, screen, type = 0, image = "card1.png" ):
		self.type = type
		self.tag = None
		self.step = 0
		self.category = 0
		self.image = image
		self.image2 = "card.png"
		self.bigImage = None
		self.screen = screen

		self.setTag()
		self.setBigImage()
	
	def setType(self, type):
		self.type = type
		self.setTag()

	def getType(self):
		return self.type
	
	def setStep(self, step):
		self.step = step
	
	def getStep(self):
		return self.step
	
	def setImage(self, image):
		self.image = image
	
	def setImageFloat(self, image):
		self.image2 = image
	
	def getImage(self):
		return self.image
	
	def getImageFloat(self):
		return self.image2
	
	def setBigImage(self, scale = 0.3):
		self.bigImage = pygame.transform.scale(self.bigImage, (int(self.bigImage.get_size()[0] * scale * 0.9), int(self.bigImage.get_size()[1] * scale * 0.9)) )
	
	def drawBigImage(self, position = (0,0)):
		self.screen.blit( self.bigImage, position )
	

	def setTag(self):
		
		self.bigImage = str(self.type) + ".png"
		self.bigImage = pygame.image.load( self.bigImage )
		
		if -1 < self.type < 24:
			self.category = 0
		
		else:
			self.category = 1
			self.step = 0
		
		if self.type == 0:
			self.step = 2
			self.tag = "Choose a Turtle +2"

		if self.type == 1:
			self.step = 1
			self.tag = "Choose a Turtle +1"
		
		if self.type == 2:
			self.step = -1
			self.tag = "Choose a Turtle -1"
		
		if self.type == 3:
			self.step = -2
			self.tag = "Choose a Turtle -2"
		
		if self.type == 4:
			self.step = 2
			self.tag = "Yellow Turtle +2"
		
		if self.type == 5:
			self.step = 1
			self.tag = "Yellow Turtle +1"
		
		if self.type == 6:
			self.step = -1
			self.tag = "Yellow Turtle -1"
		
		if self.type == 7:
			self.step = -2
			self.tag = "Yellow Turtle -2"
		
		if self.type == 8:
			self.step = 2
			self.tag = "Purple Turtle +2"
		
		if self.type == 9:
			self.step = 1
			self.tag = "Purple Turtle +1"
		
		if self.type == 10:
			self.step = -1
			self.tag = "Purple Turtle -1"
		
		if self.type == 11:
			self.step = -2
			self.tag = "Purple Turtle -2"
		
		if self.type == 12:
			self.step = 2
			self.tag = "Red Turtle +2"
		
		if self.type == 13:
			self.step = 1
			self.tag = "Red Turtle +1"
		
		if self.type == 14:
			self.step = -1
			self.tag = "Red Turtle -1"
		
		if self.type == 15:
			self.step = -2
			self.tag = "Red Turtle -2"
		
		if self.type == 16:
			self.step = 2
			self.tag = "Green Turtle +2"
		
		if self.type == 17:
			self.step = 1
			self.tag = "Green Turtle +1"
		
		if self.type == 18:
			self.step = -1
			self.tag = "Green Turtle -1"
		
		if self.type == 19:
			self.step = -2
			self.tag = "Green Turtle -2"
		
		if self.type == 20:
			self.step = 2
			self.tag = "Blue Turtle +2"
		
		if self.type == 21:
			self.step = 1
			self.tag = "Blue Turtle +1"
		
		if self.type == 22:
			self.step = -1
			self.tag = "Blue Turtle -1"
				
		if self.type == 23:
			self.step = -2
			self.tag = "Blue Turtle -2"
			
		if self.type == 24:
			self.tag = "The Fastest -2"
		
		if self.type == 25:
			self.tag = "The Fastest -1"
				
		if self.type == 26:
			self.tag = "The Slowest +1"

		if self.type == 27:
			self.tag = "The Slowest +2"
		
		if self.type == 28:
			self.tag = "Flip the Fastest Turtle"
		
		if self.type == 29:
			self.tag = "Switch the Second Turtle and the Second Last Turtle"
				
		if self.type == 30:
			self.tag = "Show the Position of a Random Pitfall"

		if self.type == 31:
			self.tag = "Remove a Random Pitfall"
		
		if self.type == 32:
			self.tag = "Play a Random Card"

		if self.type == 33:
			self.tag = "Set a Random Pitfall"








		if self.type == 34:
			self.tag = "Set a Visible Pitfall"

		if self.type == 35:
			self.tag = "Move a Turtle in a Stack to the Top"
		
		if self.type == 36:
			self.tag = "Move a Turtle in a Stack to the Bottom"

		if self.type == 37:
			self.tag = "Move Two Turtles to the Midpoint of Their Positions"

		if self.type == 38:
			self.tag = "Exchange the Positions of Two Adjacent Turtles"

		if self.type == 39:
			self.tag = "Exchange the Positions of the Second Turtle and the last but one turtle"

		if self.type == 40:
			self.tag = "The Selected Turtle is Not Affected by the Next Pitfall"

		if self.type == 41:
			self.tag = "Flip a Turtle"

		if self.type == 42:
			self.tag = "Flip the Fastest Turtle"

		if self.type == 43:
			self.tag = "Play a Random Spell Card"

		if self.type == 44:
			self.tag = "Select a Grid and the Turtles Will Take One Step Back When Reach That Grid (One-off) "

	def getTag(self):
		return self.tag

	def getCategory(self):
		return self.category


if __name__ == "__main__":

	card = Card(12)

	print "Tag: ", card.getTag()
	print "Type: ", card.getType()
	print "Step: ", card.getStep()
	print "Category: ", card.getCategory()

	card.setType(40)

	print "Tag: ", card.getTag()
	print "Type: ", card.getType()
	print "Step: ", card.getStep()
	print "Category: ", card.getCategory()

