# Yin Li
# Jan 9, 2017
# Agents existing in Turtle Go

import pygame
import sys

class Agent:
    '''general class of an agent'''
    def __init__(self,p = (0,0),f = '',v = True,i = None,g = 0):
        self.position = p
        self.file = f
        self.vis = v
        self.ima = i
        self.grid = g

    def setPosition(self, newPosition):
        self.position = newPosition

    def setVis(self, newVis):
        self.vis = newVis

    def setFile(self, newFile):
        self.file = newFile

    def setGrid(self, newGrid):
        self.grid = newGrid

    def getPosition(self):
        return self.position

    def getVis(self):
        return self.vis

    def getFile(self):
        return self.file

    def getGrid(self):
        return self.grid

    def read(self):
        '''read the image of the agent'''
        self.ima = pygame.image.load(self.file)

    def draw(self, screen):
        '''draw the agent at the given screen'''
        screen.blit(self.ima, self.position)
        pygame.display.update()class Slot(Agent):
    def __init__(self,p = (0,0),f = '',v = True,i = None,g = 0):
        self.position = p
        self.file = f
        self.vis = v
        self.ima = i
        self.grid = g
        self.hasCard = False
        self.cardType = None

    def deal(self, deck, screen):
        if self.hasCard == False:
            self.cardType = deck.deal()
            self.ima = pygame.image.load(self.cardType.getImage())
            self.hasCard = True
            self.draw(screen)

    def use(self,screen,grids,deck,turtles,slots):        
        screen.fill((255,255,255))
        for i in grids:
            i.draw(screen)
        self.cardType.use(grids,screen)
        for i in turtles:
            i.update(grids,screen)
        self.hasCard = False
        self.deal(deck,screen)
        for i in slots:
            i.draw(screen)

        





def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.font.init()
    afont = pygame.font.SysFont('Helvetica',32,bold=True)
    text = afont.render('Click To Start',True,(0,0,0))
    card = pygame.image.load('card.png')
    screen.fill((255,255,255))
    screen.blit(text,(220,200))
    pygame.display.update()

    while 1:
        for event in pygame.event.get():
            print 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                grd1 = Grid()
                grd1.setGrid(0)
                grd1.setPosition((0,0))
                grd1.setFile('grid.bmp')
                grd1.read()
                grd1.draw(screen)
                grd2 = Grid()
                grd2.setGrid(1)

                grd2.setPosition((0,100))
                grd2.setFile('grid.bmp')
                grd2.read()
                grd2.draw(screen)
                grd3 = Grid()
                grd3.setGrid(2)
                grd3.setPosition((0,200))
                grd3.setFile('grid.bmp')
                grd3.read()
                grd3.draw(screen)
                grd4 = Grid()
                grd4.setGrid(3)
                grd4.setPosition((0,300))
                grd4.setFile('grid.bmp')
                grd4.read()
                grd4.draw(screen)
                
                pygame.display.update()
                
                grd1.setTurtle([1,2,3,4,5])
                grd3.setIsTrap(True)
                grds = [grd1,grd2,grd3,grd4]
                
                t1 = Turtle()
                t1.setTurtleNum(1)
                t1.setFile('squareR.png')
                t1.read()
                t1.setPosition((0,300))
                t1.draw(screen)

                t2 = Turtle()
                t2.setTurtleNum(2)
                t2.setFile('squareB.png')
                t2.read()
                t2.setPosition((100,300))
                t2.draw(screen)

                t3 = Turtle()
                t3.setTurtleNum(3)
                t3.setFile('squareG.png')
                t3.read()
                t3.setPosition((200,300))
                t3.draw(screen)

                t4 = Turtle()
                t4.setTurtleNum(4)
                t4.setFile('squareY.png')
                t4.read()
                t4.setPosition((300,300))
                t4.draw(screen)

                t5 = Turtle()
                t5.setTurtleNum(5)
                t5.setFile('squareP.png')
                t5.read()
                t5.setPosition((400,300))
                t5.draw(screen)
                print grd1.getTurtle()
                print grd2.getTurtle()
                print grd3.getTurtle()
                print grd4.getTurtle()
                print

                pygame.time.delay(1500)
                screen.fill((255,255,255))
                for i in grds:
                    i.draw(screen)
                
                t2.moveForward(1,grds)
                t1.update(grds,screen)
                t2.update(grds,screen)
                t3.update(grds,screen)
                t4.update(grds,screen)
                t5.update(grds,screen)

                print grd1.getTurtle()
                print grd2.getTurtle()
                print grd3.getTurtle()
                print grd4.getTurtle()
                print

                pygame.time.delay(1500)
                screen.fill((255,255,255))
                for i in grds:
                    i.draw(screen)
                
                t5.moveForward(-1,grds)
                t1.update(grds,screen)
                t2.update(grds,screen)
                t3.update(grds,screen)
                t4.update(grds,screen)
                t5.update(grds,screen)

                print grd1.getTurtle()
                print grd2.getTurtle()
                print grd3.getTurtle()
                print grd4.getTurtle()
                print

                pygame.time.delay(1500)
                screen.fill((255,255,255))
                for i in grds:
                    i.draw(screen)
                
                t4.moveForward(1,grds)
                t1.update(grds,screen)
                t2.update(grds,screen)
                t3.update(grds,screen)
                t4.update(grds,screen)
                t5.update(grds,screen)

                print grd1.getTurtle()
                print grd2.getTurtle()
                print grd3.getTurtle()
                print grd4.getTurtle()
                print 

                pygame.time.delay(1500)
                screen.fill((255,255,255))
                for i in grds:
                    i.draw(screen)
                
                t5.moveForward(1,grds)
                t1.update(grds,screen)
                t2.update(grds,screen)
                t3.update(grds,screen)
                t4.update(grds,screen)
                t5.update(grds,screen)

                print grd1.getTurtle()
                print grd2.getTurtle()
                print grd3.getTurtle()
                print grd4.getTurtle()
                print

                pygame.quit()
                sys.exit()


def pygameTest():
    pygame.init()
    a = Agent()
    screen = pygame.display.set_mode((640, 480))
    screen.fill((255,255,255))
    a.setPosition((200,200))
    a.setFile('square.png')
    a.read()
    a.draw(screen)
    pygame.display.update()
    print 12
    while True:
        for evt in pygame.event.get():
                if evt.type == pygame.MOUSEBUTTONDOWN:
                    sys.exit()
    print "Terminating"

if __name__ == '__main__':
    main()
