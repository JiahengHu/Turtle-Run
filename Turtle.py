# Liwei Jiang, Yin Li, Kebing Li
# CS269 JP17
# Computer Game Design
# Turtle.py
# Jan. 15th 2017

import pygame

class Turtle:
    '''the class of turtle'''
    def __init__(self, screen, position = (0,0), color = 0, scale = 1, grid = -1):
        self.screen = screen
        self.position = position
        self.color = color
        self.image = None
        self.imagePile = None
        self.imageFlip = None
        self.imagePhoto = None
        self.scale = scale
        self.immune = False
        
        self.grid = grid
        self.trap = False
        self.trapTurn = None
        self.setImage()
    
    def setImage(self):
        if self.color == 0:
            self.image = pygame.image.load( "turtle1.png" )
            self.image = pygame.transform.scale(self.image, (int(self.image.get_size()[0] * self.scale), int(self.image.get_size()[1] * self.scale)) )
            self.imagePile = pygame.image.load( "pile1.png" )
            self.imagePile = pygame.transform.scale(self.imagePile, (int(self.imagePile.get_size()[0] * self.scale), int(self.imagePile.get_size()[1] * self.scale)) )
            self.imageFlip = pygame.image.load( "flip1.png" )
            self.imageFlip = pygame.transform.scale(self.imageFlip, (int(self.imageFlip.get_size()[0] * self.scale), int(self.imageFlip.get_size()[1] * self.scale)) )
            self.imagePhoto = pygame.image.load( "photo1.png" )
            self.imagePhoto = pygame.transform.scale(self.imagePhoto, (int(self.imagePhoto.get_size()[0] * self.scale), int(self.imagePhoto.get_size()[1] * self.scale)) )



        if self.color == 1:
            self.image = pygame.image.load( "turtle2.png" )
            self.image = pygame.transform.scale(self.image, (int(self.image.get_size()[0] * self.scale), int(self.image.get_size()[1] * self.scale)) )
            self.imagePile = pygame.image.load( "pile2.png" )
            self.imagePile = pygame.transform.scale(self.imagePile, (int(self.imagePile.get_size()[0] * self.scale), int(self.imagePile.get_size()[1] * self.scale)) )
            self.imageFlip = pygame.image.load( "flip2.png" )
            self.imageFlip = pygame.transform.scale(self.imageFlip, (int(self.imageFlip.get_size()[0] * self.scale), int(self.imageFlip.get_size()[1] * self.scale)) )
            self.imagePhoto = pygame.image.load( "photo2.png" )
            self.imagePhoto = pygame.transform.scale(self.imagePhoto, (int(self.imagePhoto.get_size()[0] * self.scale), int(self.imagePhoto.get_size()[1] * self.scale)) )


        if self.color == 2:
            self.image = pygame.image.load( "turtle3.png" )
            self.image = pygame.transform.scale(self.image, (int(self.image.get_size()[0] * self.scale), int(self.image.get_size()[1] * self.scale)) )
            self.imagePile = pygame.image.load( "pile3.png" )
            self.imagePile = pygame.transform.scale(self.imagePile, (int(self.imagePile.get_size()[0] * self.scale), int(self.imagePile.get_size()[1] * self.scale)) )
            self.imageFlip = pygame.image.load( "flip3.png" )
            self.imageFlip = pygame.transform.scale(self.imageFlip, (int(self.imageFlip.get_size()[0] * self.scale), int(self.imageFlip.get_size()[1] * self.scale)) )
            self.imagePhoto = pygame.image.load( "photo3.png" )
            self.imagePhoto = pygame.transform.scale(self.imagePhoto, (int(self.imagePhoto.get_size()[0] * self.scale), int(self.imagePhoto.get_size()[1] * self.scale)) )


        if self.color == 3:
            self.image = pygame.image.load( "turtle4.png" )
            self.image = pygame.transform.scale(self.image, (int(self.image.get_size()[0] * self.scale), int(self.image.get_size()[1] * self.scale)) )
            self.imagePile = pygame.image.load( "pile4.png" )
            self.imagePile = pygame.transform.scale(self.imagePile, (int(self.imagePile.get_size()[0] * self.scale), int(self.imagePile.get_size()[1] * self.scale)) )
            self.imageFlip = pygame.image.load( "flip4.png" )
            self.imageFlip = pygame.transform.scale(self.imageFlip, (int(self.imageFlip.get_size()[0] * self.scale), int(self.imageFlip.get_size()[1] * self.scale)) )
            self.imagePhoto = pygame.image.load( "photo4.png" )
            self.imagePhoto = pygame.transform.scale(self.imagePhoto, (int(self.imagePhoto.get_size()[0] * self.scale), int(self.imagePhoto.get_size()[1] * self.scale)) )


        if self.color == 4:
            self.image = pygame.image.load( "turtle5.png" )
            self.image = pygame.transform.scale(self.image, (int(self.image.get_size()[0] * self.scale), int(self.image.get_size()[1] * self.scale)) )
            self.imagePile = pygame.image.load( "pile5.png" )
            self.imagePile = pygame.transform.scale(self.imagePile, (int(self.imagePile.get_size()[0] * self.scale), int(self.imagePile.get_size()[1] * self.scale)) )
            self.imageFlip = pygame.image.load( "flip5.png" )
            self.imageFlip = pygame.transform.scale(self.imageFlip, (int(self.imageFlip.get_size()[0] * self.scale), int(self.imageFlip.get_size()[1] * self.scale)) )
            self.imagePhoto = pygame.image.load( "photo5.png" )
            self.imagePhoto = pygame.transform.scale(self.imagePhoto, (int(self.imagePhoto.get_size()[0] * self.scale), int(self.imagePhoto.get_size()[1] * self.scale)) )


    def setTrapTurn(self, turn):
        self.trapTurn = turn
    
    def getTrapTurn(self):
        return self.trapTurn

    def getImage(self):
        return self.image

    def getImagePile(self):
        return self.imagePile

    def getImageFlip(self):
        return self.imageFlip
    
    def getImagePhoto(self):
        return self.imagePhoto

    def getTrap(self):
        return self.trap
    
    def setTrap(self, trap):
        self.trap = trap

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setPosition(self, position):
        self.position = position

    def getPosition(self):
        return self.position

    def setGrid(self, grid):
        self.grid = grid

    def getGrid(self):
        return self.grid
        
    def setImmune(self,newImmune):
        self.immune = newImmune

    def getImmune(self):
        return self.immune

    def draw(self, position):
        self.screen.blit( self.image, position )

    def drawPile(self, position):
        self.screen.blit( self.imagePile, position)

    def drawFlip(self, position):
        self.screen.blit( self.imageFlip, position )

    def drawPhoto(self, position):
        self.screen.blit( self.imagePhoto, position )


    def ifSelected(self, mouse):
        range = self.getDimension()

        if range[0] < mouse[0] < range[1] and range[2] < mouse[1] < range[3]:
            return True
        else:
            return False
            
    def getDimension(self):
        width = self.image.get_size()[0]
        height = self.image.get_size()[1]
        
        lowX = self.position[0]
        highX = self.position[0] + int(width)
        lowY = self.position[1]
        highY = self.position[1] + int(height)

        return [lowX, highX, lowY, highY, width, height]






