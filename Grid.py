# Liwei Jiang, Yin Li, Kebing Li
# CS269 JP17
# Computer Game Design
# Grid.py
# Jan. 15th 2017

import pygame

class Grid():

    def __init__(self, screen, position = (0,0), image = "grid.png", image2 = "grid2.png", trapImage = "trap.png", scale = 1, trap = False):
        self.position = position
        self.image = image
        self.turtle = []
        self.trap = trap
        self.scale = scale
        self.screen = screen
        self.trapImage = trapImage
        
        self.image2 = image2
        
        self.turn = -1
        self.trapVisible = False
        self.setImage()
    
    def setImage(self):
        self.image = pygame.image.load( self.image )
        self.image = pygame.transform.scale(self.image, (int(self.image.get_size()[0] * self.scale), int(self.image.get_size()[1] * self.scale)) )
        self.image2 = pygame.image.load( self.image2 )
        self.image2 = pygame.transform.scale(self.image2, (int(self.image2.get_size()[0] * self.scale), int(self.image2.get_size()[1] * self.scale)) )
        self.trapImage = pygame.image.load( self.trapImage )
        self.trapImage = pygame.transform.scale(self.trapImage, (int(self.trapImage.get_size()[0] * self.scale * 0.5), int(self.trapImage.get_size()[1] * self.scale * 0.5)) )

    def setTurtle(self, turtle):
        self.turtle = turtle

    def getTurtle(self):
        return self.turtle
    
    def setTrapVisible(self, trapVisible):
        self.trapVisible = trapVisible

    def getTrapVisible(self):
        return self.trapVisible 
        
    def setTurn(self, turn):
        self.turn = turn
    
    def getTurn(self):
        return self.turn

    def setTrap(self, trap):
        self.trap = trap
    
    def getTrap(self):
        return self.trap
    
    def addTurtle(self, turtle):
        self.turtle.append(turtle)

    def swapTurtle(self, turtle1, turtle2):
        index1 = self.turtle.index(turtle1)
        index2 = self.turtle.index(turtle2)
        
        tempTurtle1 = turtle1
        
        self.turtle[index1] = turtle2
        self.turtle[index2] = tempTurtle1

    def insertTurtle(self, index, turtle):
        self.turtle.insert(index, turtle)


    def getTurtleStack(self, turtle):
        index = self.turtle.index(turtle)
        stack = []
        for i in range(index, len(self.turtle)):
            stack.append(self.turtle[i])
        return stack

    def removeTurtle(self, turtle):
        self.turtle.remove(turtle)

    def draw(self):

        if not self.trap:
            for x in self.turtle:
                x.setTrap(False)
            if len(self.turtle) == 0:
                self.screen.blit( self.image, self.position )
                    
            elif len(self.turtle) == 1:
                self.screen.blit( self.image, self.position )
                self.turtle[0].draw(self.position)
                    
            else:
                self.screen.blit( self.image, self.position )
                for i in range(len(self.turtle)):
                    self.turtle[i].drawPile((self.position[0], self.position[1] - 25*i))

        elif self.trap:

            if len(self.turtle) == 0:
                self.screen.blit( self.image, self.position )
                if self.getTrapVisible() == True:
                    self.screen.blit( self.trapImage, self.position )

            elif len(self.turtle) == 1:
                self.screen.blit( self.image, self.position )
                self.screen.blit( self.trapImage, self.position )
                self.turtle[0].drawFlip(self.position)
                self.turtle[0].setTrap(True)

            else:
                self.trap = False
                self.screen.blit( self.image, self.position )
                for i in range(len(self.turtle)):
                    self.turtle[i].drawPile((self.position[0], self.position[1] - 25*i))
##                    self.turtle[i].setTrap(False)
##                    self.turtle[i].setTrapTurn(-1)
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

    def draw2(self):

        if not self.trap:
            for x in self.turtle:
                x.setTrap(False)
            if len(self.turtle) == 0:
                self.screen.blit( self.image2, self.position )
                    
            elif len(self.turtle) == 1:
                self.screen.blit( self.image2, self.position )
                self.turtle[0].draw(self.position)
                    
            else:
                self.screen.blit( self.image2, self.position )
                for i in range(len(self.turtle)):
                    self.turtle[i].drawPile((self.position[0], self.position[1] - 25*i))

        elif self.trap:

            if len(self.turtle) == 0:
                self.screen.blit( self.image2, self.position )
                if self.getTrapVisible() == True:
                    self.screen.blit( self.trapImage, self.position )

            elif len(self.turtle) == 1:
                self.screen.blit( self.image2, self.position )
                self.screen.blit( self.trapImage, self.position )
                self.turtle[0].drawFlip(self.position)
                self.turtle[0].setTrap(True)

            else:
                self.trap = False
                self.screen.blit( self.image2, self.position )
                for i in range(len(self.turtle)):
                    self.turtle[i].drawPile((self.position[0], self.position[1] - 25*i))
##                    self.turtle[i].setTrap(False)
##                    self.turtle[i].setTrapTurn(-1)


















