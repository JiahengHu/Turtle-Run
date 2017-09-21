# Liwei Jiang, Yin Li, Kebing Li
# CS269 JP17
# Computer Game Design
# Slot.py
# Jan. 16th 2017

import Card
import Deck
import pygame

class Slot():
    def __init__(self, ID = 0, position = (0,0), screen = None, scale = 0.2, deck = None, dimension = [0,0,0,0]):
        self.ID = ID
    	self.position = position
        self.card = None
        self.deck = deck
        self.dimension = dimension
        self.screen = screen
        self.scale = scale
        self.image = None
        self.imageFloat = None
        self.deal()

    def getID(self):
        return self.ID
        
    def setID(self, id):
        self.ID = id

    def getPosition(self):
		return self.position

    def setPosition(self, position):
		self.position = position
    
    def setDimension(self, dimension):
        self.dimension = dimension
    
    def getDimension():
        return self.dimension
    
    def draw(self):
        self.screen.blit( self.image, self.position )
    
    def drawFloat(self):
        self.screen.blit( self.imageFloat, self.position )

    def setScale(self, scale):
        self.scale = scale
    
    def getScale(self):
        return self.scale
    
    def getImage(self):
        return self.image

    def getImageFloat(self):
        return self.imageFloat

    def getCard(self):
        return self.card
    
    def getCardType(self):
        return self.card.getType()
        
    def addCard(self, card):
    	self.card = card
    	self.image = pygame.image.load( self.card.getImage() )
        self.imageFloat = pygame.image.load( self.card.getImageFloat() )
    	self.image = pygame.transform.scale(self.image, (int(self.image.get_size()[0]*0.2), int(self.image.get_size()[1]*0.2)) )
        self.imageFloat = pygame.transform.scale(self.imageFloat, (int(self.imageFloat.get_size()[0]*0.2), int(self.imageFloat.get_size()[1]*0.2)) )
        
    
    def getDimension(self):
        width = self.image.get_size()[0]
        height = self.image.get_size()[1]
        
        lowX = self.position[0]
        highX = self.position[0] + int(width)
        lowY = self.position[1]
        highY = self.position[1] + int(height)
        
        return [lowX, highX, lowY, highY, width, height]
    
    def ifSelected(self, mouse):
        range = self.getDimension()
        
        if range[0] < mouse[0] < range[1] and range[2] < mouse[1] < range[3]:
            return True
        else:
            return False
    
    def deal(self):
    	oldCard = self.card
        self.card = self.deck.deal()
        self.image = pygame.image.load( self.card.getImage() )
        self.imageFloat = pygame.image.load( self.card.getImageFloat() )
            
        self.image = pygame.transform.scale(self.image, (int(self.image.get_size()[0]*0.2), int(self.image.get_size()[1]*0.2)) )
        self.imageFloat = pygame.transform.scale(self.imageFloat, (int(self.imageFloat.get_size()[0]*0.2), int(self.imageFloat.get_size()[1]*0.2)) )
        
        return self.card, oldCard




