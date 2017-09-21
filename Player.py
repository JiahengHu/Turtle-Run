# Liwei Jiang, Yin Li, Kebing Li
# CS269 JP17
# Computer Game Design
# Player.py
# Jan. 12th 2017

import pygame

class Player:

	def __init__(self, screen, turtle, player = 0, score = 0, image = "icon.png", imageFloat = "icon1.png", imageClick1 = "icon3.png", imageClick2 = "icon4.png", imageWon = "playerWon1.png", position = (0,0), scale = 1):
		self.image = image
		self.imageFloat = imageFloat
		self.imageClick = imageClick1
		self.imageClick2 = imageClick2
		
		self.playerID = player
		self.position = position
		self.scale = scale
		self.screen = screen
		self.dimension = []
		self.toggle = True
		self.turtle = turtle	
		self.imageWon = None  
		self.score = score
		self.imageScore = None
		self.scoreToggle = True
		self.imageLabel = None
		 
		self.setImageScore() 
		self.setImageWon()	  
		self.setImage()

	def setImageWon(self):
		
		fileName = "playerWon" + str(self.playerID + 1) + ".png"
		self.imageWon = pygame.image.load(fileName)
		self.imageWon = pygame.transform.scale(self.imageWon, (int(self.imageWon.get_size()[0]*self.scale*2), int(self.imageWon.get_size()[1]*self.scale*2)) )
		fileName = "playerLabel" + str(self.playerID + 1) + ".png"
		self.imageLabel = pygame.image.load(fileName)
		self.imageLabel = pygame.transform.scale(self.imageLabel, (int(self.imageLabel.get_size()[0]*self.scale*0.2), int(self.imageLabel.get_size()[1]*self.scale*0.2)) )
		

	def setImageScore(self):
		self.imageScore = "PS" + str(self.playerID + 1) + ".png"
		self.imageScore = pygame.image.load(self.imageScore)
		self.imageScore = pygame.transform.scale(self.imageScore, (int(self.imageScore.get_size()[0]*self.scale*4), int(self.imageScore.get_size()[1]*self.scale*4)) )

	
	def setScoreToggle(self, toggle):
		self.scoreToggle = toggle
	
	def getScoreToggle(self):
		return self.scoreToggle
	
	
	def setScore(self, score):
		self.score = score
		
	def getScore(self):
		return self.score

	def setImage(self):
		self.image = pygame.image.load( self.image )
		self.imageFloat = pygame.image.load( self.imageFloat )
		self.imageClick = pygame.image.load( self.imageClick )
		self.imageClick2 = pygame.image.load( self.imageClick2 )

		self.image = pygame.transform.scale(self.image, (int(self.image.get_size()[0]*self.scale), int(self.image.get_size()[1]*self.scale)) )
		self.imageFloat = pygame.transform.scale(self.imageFloat, (int(self.imageFloat.get_size()[0]*self.scale), int(self.imageFloat.get_size()[1]*self.scale)))
		self.imageClick = pygame.transform.scale(self.imageClick, (int(self.imageFloat.get_size()[0] * 1.2), int(self.imageFloat.get_size()[1] * 1.2)))
		self.imageClick2 = pygame.transform.scale(self.imageClick2, (int(self.imageFloat.get_size()[0] * 1.2), int(self.imageFloat.get_size()[1] * 1.2)))
	
	
	def setTurtle(self, turtle):
		self.turtle = turtle
	
	def getTurtle(self):
		return self.turtle
	
	def setPlayer(self, player):
		self.player = player
		
	def getPlayer(self):
		return self.player
	
	def setPosition(self, position):
		self.position = position
	
	def getToggle(self):
		return self.toggle
	
	def setToggle(self, toggle):
		self.toggle = toggle
	
	def getPosition(self):
		return self.position

	def setScale(self, scale):
		self.scale = scale

	def getScale(self):
		return self.scale

	def getImage(self):
		return self.image

	def getImageFloat(self):
		return self.imageFloat
	
	def getImageClick(self):
		return self.imageClick
		
	def getImageClick2(self):
		return self.imageClick2		
		
	def getImageWon(self):
		return self.imageWon
		
	def getImageScore(self):
		return self.imageScore
	
	def getImageLabel(self):
		return self.imageLabel
	
	
	def getDimension(self):
		width = self.image.get_size()[0]
		height = self.image.get_size()[1]
		
		lowX = self.position[0]
		highX = self.position[0] + int(width)
		lowY = self.position[1]
		highY = self.position[1] + int(height)

		return [lowX, highX, lowY, highY, width, height]

	def drawPlayer(self):
		self.screen.blit( self.image, self.position )
		self.screen.blit( self.imageLabel, (self.position[0] - 40, self.position[1]) )
		
	def drawPlayerFloat(self):
		self.screen.blit( self.imageFloat, self.position )
		self.screen.blit( self.imageLabel, (self.position[0] - 40, self.position[1]) )
		
	def drawPlayerClick(self):	
		self.screen.blit( self.imageClick, (self.position[0] - 5, self.position[1] - 23 ) )
		self.screen.blit( self.imageLabel, (self.position[0] - 40, self.position[1]) ) 
		
	def drawPlayerClick2(self):	
		self.screen.blit( self.imageClick2, (self.position[0] - 5, self.position[1] - 23 ) )
		self.screen.blit( self.imageLabel, (self.position[0] - 40, self.position[1]) ) 
			
		
	def drawPlayerWon(self, position):
		self.screen.blit( self.imageWon, position )
		
	def drawPlayerScore(self, position):
		self.screen.blit( self.imageScore, position )
		
	def drawPlayerLabel(self, position):
		self.screen.blit( self.imageLabel, position )

	def ifSelected(self, mouse):
		range = self.getDimension()

		if range[0] < mouse[0] < range[1] and range[2] < mouse[1] < range[3]:
			return True
		else:
			return False












