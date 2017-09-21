# Liwei Jiang, Yin Li, Kebing Li
# CS269 JP17
# Computer Game Design
# Button.py
# Jan. 16th 2017

import pygame



class Button:

    def __init__(self, screen, image = "click1.png", imageFloat = "click2.png", imageClick = "buttonClick.png", position = (0,0), scale = 1):
        self.image = image
        self.imageFloat = imageFloat
        self.imageClick = imageClick
        self.position = position
        self.scale = scale
        self.screen = screen
        self.dimension = []
        self.toggle = True
        self.setImage()

    def setImage(self):
        self.image = pygame.image.load( self.image )
        self.imageFloat = pygame.image.load( self.imageFloat )
        self.imageClick = pygame.image.load( self.imageClick )

        self.image = pygame.transform.scale(self.image, (int(self.image.get_size()[0]*self.scale), int(self.image.get_size()[1]*self.scale)) )
        self.imageFloat = pygame.transform.scale(self.imageFloat, (int(self.imageFloat.get_size()[0]*self.scale), int(self.imageFloat.get_size()[1]*self.scale)))
    	self.imageClick = pygame.transform.scale(self.imageClick, (int(self.imageClick.get_size()[0]*self.scale), int(self.imageClick.get_size()[1]*self.scale)))
    
    
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
	
    def getDimension(self):
        width = self.image.get_size()[0]
        height = self.image.get_size()[1]
        
        lowX = self.position[0]
        highX = self.position[0] + int(width)
        lowY = self.position[1]
        highY = self.position[1] + int(height)

        return [lowX, highX, lowY, highY, width, height]

    def drawButton(self):
        self.screen.blit( self.image, self.position )
        
    def drawButtonFloat(self):
        self.screen.blit( self.imageFloat, self.position )
        
    def drawButtonClick(self):  
    	self.screen.blit( self.imageClick, self.position ) 

    def ifSelected(self, mouse):
        range = self.getDimension()

        if range[0] < mouse[0] < range[1] and range[2] < mouse[1] < range[3]:
            return True
        else:
            return False












