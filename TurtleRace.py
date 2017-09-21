# Liwei Jiang
# January 2017
# CS269 Computer Game Design
# Turtle Races

# import
import sys
import time
import pygame
import Deck
import Card
import Slot
import Button
import Grid
import Turtle
import Music
import random
import time
import Player

#import agent
class TurtleRace:
	
	def __init__(self):
		self.background = None
		self.icon = None
		self.caption = None
		
		self.screen = None
		self.gameBoard = None
		self.pauseBoard = []
		self.finishBoard = []
		
		
		self.startButton = None
		self.instructionButton = None
		self.quitButton = None
		self.endButton = None
		self.newButton = None
		self.returnButton = None
		self.peekButton = None
		self.informationButton = None
		self.mode = None

		self.scene = 0
		self.deck = None
		self.slot = []
		
		self.players = []
	
		self.turtles = []
		
		self.instruction = None
		self.cardIndex = None
	
		self.click1Music = None
		self.click2Music = None
		self.startMusic = None
		self.instructionMusic = None
		self.game1Music = None
		self.endMusic = None
		
		
		self.startMusicOn = True
		self.instructionMusicOn = True
		self.game1MusicOn = True
		
		self.channel1 = None
		self.channel2 = None

		self.grids = []
	
		self.turn = 0
			
		self.currentUser = 0
		
		self.ifUserStart = True
		
		self.userOn = True
		
		self.instructionWindow = None
		
		self.informationWindow = None
		
		self.guideWindow = None
		
		self.oldCard = None
	
		self.gameBoard2 = None	
		self.mode = 0
		
		

	# initialize the game scene #
	def initialize(self):
		pygame.init()
		pygame.mixer.init()
		
		try:
			pygame.font.init()
		except:
			print "Fonts unavailable"
			sys.exit()
		self.loadMusic()



################################################################# load music ################################################################

	def loadMusic(self):
		self.channel1 = pygame.mixer.Channel(0)
		self.channel2 = pygame.mixer.Channel(1)
		
		self.instructionMusic = Music.Music(self.channel1, "instruction.wav")
		self.click1Music = Music.Music(self.channel2, "click1.wav")
		self.click2Music = Music.Music(self.channel2, "click2.wav")
		self.startMusic = Music.Music(self.channel1, "start.wav")
		
		self.game1Music = Music.Music(self.channel1, "game1.wav")
		self.game2Music = Music.Music(self.channel1, "game2.wav")
		
		self.endMusic = Music.Music(self.channel1, "victory.wav")
		
	
################################################################# scene 0: start scene ################################################################

	# set the background of start screen #
	def setStartScreenBackground(self):
		self.background = pygame.image.load( "background.jpg" )
		self.icon = pygame.image.load( "icon.png" )
		self.caption = "Turtle Race"
		
		# set game application icon
		pygame.display.set_icon(self.icon)
		# set caption of the game window
		pygame.display.set_caption(self.caption)
		
		# set background picture
		self.background = pygame.transform.scale(self.background, (int(self.background.get_size()[0]*0.5), int(self.background.get_size()[1]*0.5)) )
		backgroundSize = (width, height) = self.background.get_size()

		# screen (width, height)
		self.screen = pygame.display.set_mode( backgroundSize )
		self.deck = Deck.Deck(self.screen)
		
		self.informationWindow = pygame.image.load( "informationWindow.jpg" )
		self.informationWindow = pygame.transform.scale(self.informationWindow, (int(self.background.get_size()[0]), int(self.background.get_size()[1])) )
			
		self.guideWindow = pygame.image.load( "informationWindow.jpg" )
		self.guideWindow = pygame.transform.scale(self.guideWindow, (int(self.background.get_size()[0]*0.8), int(self.background.get_size()[1]*0.8)) )
		

	# draw start screem background #
	def drawStartScreenBackground(self):
		self.screen.blit( self.background, (0, 0) )
		
	def drawInformationWindow(self, position):
		self.screen.blit( self.informationWindow, position )
	
	def drawGuideWindow(self, position):
		self.screen.blit( self.guideWindow, position )

	# set start screen buttons #
	def setStartScreenButtons(self):
	
		self.startButton = Button.Button(self.screen, image = "startButton2.png", imageFloat = "startButton1.png")
		self.instructionButton = Button.Button(self.screen, image = "instructionButton2.png", imageFloat = "instructionButton1.png")
		self.quitButton = Button.Button(self.screen, image = "quitButton2.png", imageFloat = "quitButton1.png")
		
		offsetX = 400
		offsetY = 0
		self.startButton.setPosition((offsetX,offsetY))
		
		offsetY += self.startButton.getDimension()[5] - 15
		offsetX = 260
		self.instructionButton.setPosition((offsetX,offsetY))

		offsetY = 380
		offsetX = 920
		self.quitButton.setPosition((offsetX,offsetY))

	def drawStartScreenButtons(self):
		self.startButton.drawButtonFloat()
		self.instructionButton.drawButtonFloat()
		self.quitButton.drawButtonFloat()


	def setStartScreen(self):
		self.setStartScreenBackground()
		self.setStartScreenButtons()
	
	def drawStartScreen(self):
		self.drawStartScreenBackground()
	
	def drawStartScreen2(self):
		self.drawStartScreenBackground()

################################################################# scene 1: game scene ################################################################


   # set game buttons #
	def setGameButtons(self):
		self.endButton = Button.Button(self.screen, image = "returnButton2.png", imageFloat = "returnButton1.png", imageClick = "buttonClick1.png", scale = 0.9)
		self.peekButton = Button.Button(self.screen, image = "instructionButton2.png", imageFloat = "instructionButton1.png", imageClick = "buttonClick1.png", scale = 0.4)
		self.informationButton = Button.Button(self.screen, image = "informationButton2.png", imageFloat = "informationButton1.png", imageClick = "buttonClick1.png", scale = 0.4)
		self.modeButton = Button.Button(self.screen, image = "modeButton2.png", imageFloat = "modeButton1.png", imageClick = "buttonClick1.png", scale = 0.4)
		
		self.endButton.setPosition((30, 520))
		self.peekButton.setPosition((40, 0))
		self.informationButton.setPosition((400, 0))
		self.modeButton.setPosition((770, 0))
		

	# draw game buttons #
	def drawGameButtons(self, mode = 0):
		if mode == 0:
			self.endButton.drawButton()
			self.modeButton.drawButton()
		elif mode == 1:
			self.endButton.drawButton()
		elif mode == 2:
			self.modeButton.drawButton()
		self.peekButton.drawButton()
		self.informationButton.drawButton() 

	
	# set game background #
	def setGameBackground(self):
		self.gameBoard = pygame.image.load( "gameBoard.jpg" )
		self.gameBoard = pygame.transform.scale(self.gameBoard, (self.background.get_size()[0], self.background.get_size()[1]) )
		
		self.gameBoard2 = pygame.image.load( "gameBoard2.jpg" )
		self.gameBoard2 = pygame.transform.scale(self.gameBoard2, (self.background.get_size()[0], self.background.get_size()[1]) )


	def drawGameBackground(self):
		if self.mode == 0:
			self.screen.blit( self.gameBoard, (0, 0) )
		elif self.mode == 1:
			self.screen.blit( self.gameBoard2, (0, 0) )


	def setCard(self, cardNumber = 5):
		self.slot = []
		for i in range(5):
			temp = []
			for i in range(cardNumber):
				slot = Slot.Slot(i, (450 + 120 * i,530), self.screen, 0.2, self.deck)
				temp.append(slot)
			self.slot.append(temp)


	def drawCard(self):
		for i in range(5):
			self.slot[self.currentUser][i].drawFloat()


	def setPlayers(self, number):
		turtlelist = []
		
		for i in range(number):
			turtlelist.append(i)		
		random.shuffle(turtlelist)
		
		print "rebuild Player"
		
		if len(self.players) == 0:
			for i in range(number):
				character = Player.Player(screen = self.screen, score = 0, turtle = self.turtles[turtlelist[i]], player = i, position = (1115, 364 + 65 * i ), scale = 0.2)
				self.players.append(character)
		else:
			for i in range(number):
				character = Player.Player(screen = self.screen, score = self.players[i].getScore(), turtle = self.turtles[turtlelist[i]], player = i, position = (1115, 364 + 65 * i ), scale = 0.2)
				self.players[i] = character
				


	def drawPlayers(self):
		for i in range(len(self.players)):
			self.players[i].drawPlayerFloat()
#		if self.userOn:
#			self.players[self.currentUser].drawPlayerClick2()


	def setTurtles(self, number):
		self.turtles = []
		for i in range(number):
			turtle = Turtle.Turtle(self.screen, scale = 0.18, color = i)
			self.turtles.append(turtle)

	def drawTurtles(self):
		for i in range(len(self.turtles)):
			self.turtles[i].draw((1100, 72 * i ))
			self.turtles[i].setPosition((1100, 72 * i ))


	def setGrids(self, number):
		self. grids = []
		for i in range(number-1):
			if i%2 == 0:
				grid = Grid.Grid(self.screen, position = (50 + 100 * i , random.randint(280, 400)), scale = 0.4)
			else:
				grid = Grid.Grid(self.screen, position = (50 + 100 * i , random.randint(80, 150)), scale = 0.4)
								
			if random.uniform(0,1) >= 0.3:
				grid.setTrap(True)
				
			self.grids.append(grid)

		grid = Grid.Grid(self.screen, image = "gridFlag.png", image2 = "gridFlag2.png", position = (50 + 100 * (i+1) , random.randint(80, 150)), scale = 0.4)
								
		if random.uniform(0,1) >= 0.7:
			grid.setTrap(True)
				
		self.grids.append(grid)
		

	def drawGrids(self):
		for i in range(len(self.grids)):
			if self.mode == 0:
				self.grids[i].draw()
			elif self.mode == 1:
				self.grids[i].draw2()

	def setGame(self):
		self.currentUser = 0
		self.setGameBackground()
		self.setGameButtons()
		self.setCard()
		self.setGrids(10)
		self.setTurtles(5)
		self.setPlayers(5)
	
	def drawGame(self):
		self.drawGameBackground()
		self.drawGameButtons()
		self.drawCard()
		self.drawGrids()
		self.drawPlayers()
		self.drawTurtles()
		
	
	def drawGame2(self, mode = 0):
		self.drawGameBackground()
		self.drawGameButtons(mode)
		self.drawCard()
		self.drawGrids()
		self.drawPlayers()
		self.drawTurtles()
		
			
	
############################################################### scene 2: instruction scene ##############################################################

	
	def setInstructionBackground(self):
		self.instruction = pygame.image.load( "instruction.png" )
		self.instruction = pygame.transform.scale(self.instruction, (int(self.background.get_size()[0]), int(self.background.get_size()[1])) )
		self.instructionWindow = pygame.image.load( "instruction2.png" )
		self.instructionWindow = pygame.transform.scale(self.instructionWindow, (int(self.background.get_size()[0] * 1), int(self.background.get_size()[1] * 1)) )

	def drawInstructionBackground(self):
		self.screen.blit( self.instruction, (0, 0) )
		
	def drawInstructionWindow(self, position):
		self.screen.blit( self.instructionWindow, position )

	def setInstructionButtons(self):
		self.returnButton = Button.Button(self.screen, image = "returnButton2.png", imageFloat = "returnButton1.png", position = (460, 540), scale = 0.8)
	
	
	def drawInstructionButtons(self):
		self.returnButton.drawButton()

	def setInstruction(self):
		self.setInstructionBackground()
		self.setInstructionButtons()
	
	def drawInstruction(self):
		self.drawInstructionBackground()
		self.drawInstructionButtons()

	def drawInstruction2(self):
		self.drawInstructionBackground()		

################################################################# set finish scene background ################################################################


	# set game background #
	def setFinishBackground(self):
		for i in range(5):
			finishBoard = pygame.image.load( "end" + str(i+1) + ".png" )
			finishBoard = pygame.transform.scale(finishBoard, (self.background.get_size()[0], self.background.get_size()[1]) )
			self.finishBoard.append(finishBoard)
			
	def drawFinishBackground(self, turtleIndex, playerIndex):
		self.screen.blit( self.finishBoard[turtleIndex], (0, 0) ) 
		self.players[playerIndex].drawPlayerWon((30, 350))
		
	def setFinishButton(self):
		self.newButton = Button.Button(self.screen, image = "restartButton2.png", imageFloat = "restartButton1.png", scale = 0.4, position = (750, 150))
		
	def drawFinishButton(self):
		self.newButton.drawButton() 
			
	def setFinish(self):
		self.setFinishBackground()
		self.setFinishButton()
		
	def drawFinish(self, turtleIndex, playerIndex):
		self.drawFinishBackground(turtleIndex, playerIndex)
		self.drawFinishButton()

	def drawFinish2(self, index):
		self.drawFinishBackground(index)	
		
############################################################### scene 4: pause scene ##############################################################

	def setPauseBackground(self):
		self.pauseBoard = []
		for i in range(5):
			pauseBoard = pygame.image.load( "middle" + str(i + 1) + ".png" )
			pauseBoard = pygame.transform.scale(pauseBoard, (int(self.background.get_size()[0]), int(self.background.get_size()[1])) )
			self.pauseBoard.append(pauseBoard)

	def drawPauseBackground(self): 
		self.screen.blit( self.pauseBoard[self.currentUser], (0, 0) )

	def setPause(self):
		self.setPauseBackground()
	
	def drawPause(self):
		self.drawPauseBackground()


################################################################# main ################################################################

	def selectTurtle(self,ID):
		if ID in [0,1,2,3,35,36,40,41]:
			selectedTurtle = None
			while 1:
				for event in pygame.event.get():
					for i in range(5):
						if self.turtles[i].ifSelected(pygame.mouse.get_pos()) and self.scene == 1:
							if event.type == pygame.MOUSEBUTTONDOWN:
								selectedTurtle = self.turtles[i]
								return selectedTurtle

	def selectGrid(self,ID):
		if	ID in [34]:
			selectedGrid = None
			while 1:
				for event in pygame.event.get():
					for i in range(8):
						if self.grids[i].ifSelected(pygame.mouse.get_pos()) and self.scene == 1:
							if event.type == pygame.MOUSEBUTTONDOWN:
								selectedGrid = self.grids[i]
								return selectedGrid

	def action(self, ID, currentTurtle, currentGrid):
	
		if 0 <= ID <= 3:
			step = ID
			if step == 0:
				step = 2	
			elif step == 1:
				step = 1				
			elif step == 2:
				step = -1		
			elif step == 3:
				step = -2 

			if step < 0:
				if -step > currentTurtle.getGrid():
					return True
			
			elif step > 0:
				if step >= (len(self.grids) - currentTurtle.getGrid()):
					return True
				
				
			if currentTurtle.getGrid() == -1:
				if step>0:
					self.grids[step-1].addTurtle(currentTurtle)
					currentTurtle.setGrid(step-1)
				else: 
					return True
					
			else:
				curGridNum = currentTurtle.getGrid()
				curGrid = self.grids[curGridNum]
				for turtle in curGrid.getTurtleStack(currentTurtle):
					if turtle.getTrap() == True:
						curGrid.setTrap(False)
						return
					self.grids[curGridNum].removeTurtle(turtle)
					self.grids[curGridNum+step].addTurtle(turtle)
					turtle.setGrid(curGridNum+step)


		elif 4 <= ID <= 23: 
		
			step = ID%4
			if step == 0:
				step = 2	
			elif step == 1:
				step = 1				
			elif step == 2:
				step = -1		
			elif step == 3:
				step = -2	

			if step < 0:
				if -step > self.turtles[ID/4-1].getGrid():
					return True		
			elif step > 0:
				if step >= (len(self.grids) - self.turtles[ID/4-1].getGrid()):
					return True

			if self.turtles[ID/4-1].getGrid() == -1:
				if step>0:
					self.grids[step-1].addTurtle(self.turtles[ID/4-1])
					self.turtles[ID/4-1].setGrid(step-1)
				else: 
					return True

			else:
				curGridNum = self.turtles[ID/4-1].getGrid()
				curGrid = self.grids[curGridNum]
#				if len(curGrid.getTurtle()) == 1 and curGrid.getTurtle()[0].getTrap():
#					if curGrid.getTurtle()[0].getTrapTurn() == None:
#						curGrid.getTurtle()[0].setTrapTurn(self.turn)
#						return True
#					elif curGrid.getTurtle()[0].getTrapTurn() == self.turn:
#						return True
#					elif curGrid.getTurtle()[0].getTrapTurn() != self.turn:
#						curGrid.getTurtle()[0].setTrapTurn(None)
#						curGrid.getTurtle()[0].setTrap(False)
#						curGrid.setTrap(False)			
		
				for turtle in curGrid.getTurtleStack(self.turtles[ID/4-1]):
					if turtle.getTrap() == True:
						curGrid.setTrap(False)
						return
					self.grids[curGridNum].removeTurtle(turtle)
					self.grids[curGridNum+step].addTurtle(turtle)
					turtle.setGrid(curGridNum+step)



		# the fastest -2/-1 | the slowest +2/+1 #
		elif 27 >= ID >= 24:	
			step = None 
			if ID == 24:
				step = -2
			elif ID == 25:
				step = -1
			elif ID == 26:
				step = 1
			elif ID == 27:
				step = 2
			
			num = 0
			for grid in self.grids:
				if len(grid.getTurtle()) == 0:
					num += 1
			if num == len(self.grids):
				return True
			
			
			if ID == 24 or ID == 25:
				curGridNum = 0
				for turtle in self.turtles:
					if turtle.getGrid() > curGridNum:
						curGridNum = turtle.getGrid()
			else:
				curGridNum = 1000
				for turtle in self.turtles:
					if 0 <= turtle.getGrid() < curGridNum:
						curGridNum = turtle.getGrid()
						
			lastGrid = self.grids[curGridNum]
			if (curGridNum + step) < 0 or (curGridNum + step) >= len(self.grids):
				return True
				
			bottomTurtle = lastGrid.getTurtle()[0]
			if len(lastGrid.getTurtle()) == 1 and bottomTurtle.getTrap():
				if bottomTurtle.getTrapTurn() == None:
					bottomTurtle.setTrapTurn(self.turn)
					return True
				elif bottomTurtle.getTrapTurn() == self.turn:
					return True
				elif bottomTurtle.getTrapTurn() != self.turn:
					bottomTurtle.setTrapTurn(None)
					bottomTurtle.setTrap(False)		
					lastGrid.setTrap(False)		
				
			for turtle in lastGrid.getTurtleStack(bottomTurtle):
				self.grids[curGridNum].removeTurtle(turtle)
				self.grids[curGridNum + step].addTurtle(turtle)
				turtle.setGrid(curGridNum + step)	


		# flip the fastest turtle #
		elif ID == 28:
			curGridNum = 0
			for turtle in self.turtles:
				if turtle.getGrid() > curGridNum:
					curGridNum = turtle.getGrid()
				if turtle.getTrap() == True:
						return True
			
			lastGrid = self.grids[curGridNum]			
			bottomTurtle = lastGrid.getTurtle()[0]
			lastGrid = self.grids[curGridNum]
			lastGrid.setTrap(True)

		# Exchange the Positions of the Second Turtle and the last second turtle #
		elif ID == 29:
			
			num = 0
			for turtle in self.turtles:
				if turtle.getGrid() == -1:
					num+=1
			if num >= 4:
				return True		 
			
			list = []
			for grid in self.grids:
				if len(grid.getTurtle())!=0:
					list.append(grid)
					
			if len(list[-1].getTurtle())>=2:
				turtle2 = list[-1].getTurtle()[1]		
			else:
				turtle2 = list[-2].getTurtle()[0]
					
			if len(list[0].getTurtle())>=2:
				turtle1 = list[0].getTurtle()[1]
			else:
				turtle1 = list[1].getTurtle()[0]
				
			index1 = self.grids[turtle1.getGrid()].getTurtle().index(turtle1)
			index2 = self.grids[turtle2.getGrid()].getTurtle().index(turtle2)
			self.grids[turtle1.getGrid()].removeTurtle(turtle1)
			self.grids[turtle2.getGrid()].removeTurtle(turtle2)
			self.grids[turtle1.getGrid()].insertTurtle(index1,turtle2)
			self.grids[turtle2.getGrid()].insertTurtle(index2,turtle1)
			oldGrid1 = turtle1.getGrid()
			oldGrid2 = turtle2.getGrid()
			turtle1.setGrid(oldGrid2)
			turtle2.setGrid(oldGrid1)
			
		# show the position of a random pitfall #
		elif ID == 30:
			tmp = self.grids[:]
			random.shuffle(tmp)
			flag = True
			for grid in tmp:
				if grid.getTrap() == True:
					grid.setTrapVisible(True)
					flag = False
					break
			if flag:
				return True

		# remove a random pitfall #
		elif ID == 31:
			tmp = self.grids[:]
			random.shuffle(tmp)
			flag = True
			for grid in tmp:
				if grid.getTrap() == True and len(grid.getTurtle()) == 0:
					grid.setTrap(False)
					flag = False
					break
			if flag:	
				return True

		# play a random card #
		elif ID == 32:
			ID = random.randint(4,24)
			card = Card.Card(self.screen, ID)
			card.drawBigImage(position = (500, 20))
			self.action(ID,currentTurtle,currentGrid)
			
				#set a random pitfall
		elif ID == 33:
			tmp = self.grids[:]
			random.shuffle(tmp)
			flag = True
			for grid in tmp:
				if grid.getTrap() == False:
					grid.setTrap(True)
					flag = False
					break
			if flag == True:
				return True
			
		# set a visible pitfall
		elif ID == 34:
			currentGrid.setTrap(True)
			currentGrid.setTrapVisible(True)	

		# swap the turtle with the top one in the stack
		elif ID == 35:
			curGridNum = currentTurtle.getGrid()
			if curGridNum == -1:
				return True
			curGrid = self.grids[curGridNum]
			curGrid.swapTurtle(currentTurtle, curGrid.getTurtle()[-1])
		
		# swap the turtle with the bottom one in the stack
		elif ID == 36:
			curGridNum = currentTurtle.getGrid()
			if curGridNum == -1:
				return True
			curGrid = self.grids[curGridNum]
			curGrid.swapTurtle(currentTurtle, curGrid.getTurtle()[0])
			


		# selected turtle is immune to next trap
		elif ID == 40:
			currentTurtle.setImmune(True)
			
		# flip a turtle
		elif ID == 41:
			curGridNum = currentTurtle.getGrid()
			curGrid = self.grids[curGridNum]
			curGrid.setTrap(True)
		


			
		self.turn += 1
		for grid in self.grids:
			grid.setTurn(self.turn)
			
		return False


	def main(self):
		self.initialize()	
		self.setStartScreen()
		self.setGame()
		self.setInstruction()
		self.setFinish()
		self.setPause()
		self.drawStartScreen()
		pygame.display.update()
		self.mainLoop()
	
	
	

	def mainLoop(self):
		quit = True
		afont = pygame.font.SysFont( "Helvetica", 64, bold = True )

		while quit:
			for event in pygame.event.get():
				
				if len(self.grids[9].getTurtle()) != 0:
					self.scene = 3
					
				
				mousePosition = pygame.mouse.get_pos()
				mouseX = mousePosition[0]
				mouseY = mousePosition[1]

				if self.scene == 0:
					self.instructionMusic.stop()
						
					self.endMusic.stop()
					self.startMusic.play(-1)
				
					# start button #
					if self.startButton.ifSelected(mousePosition) and self.scene == 0:
						self.startButton.drawButtonFloat()
						
						if self.startButton.getToggle():
							self.click1Music.play()
							self.startButton.setToggle(False)
						
						if event.type == pygame.MOUSEBUTTONDOWN:
							self.click2Music.play()
							
							self.drawStartScreen2()
							self.startButton.drawButtonClick()
							pygame.display.update()
							time.sleep(0.6)
										
#							self.drawGuideWindow((220, 60))
#							pygame.display.update()
#							time.sleep(2)
#							
#							self.drawInformationWindow((0, 0))
#							pygame.display.update()
#							time.sleep(2)

							self.drawPause()
							self.scene = 4
							
# 							if event.type == pygame.KEYDOWN:
# 								self.scene = 1
# 								self.drawGame()

					elif not self.startButton.ifSelected(mousePosition) and self.scene == 0:
						self.startButton.drawButton()
						self.startButton.setToggle(True)


					# instruction button #
					if self.instructionButton.ifSelected(mousePosition) and self.scene == 0:
						self.instructionButton.drawButtonFloat()
						
						if self.instructionButton.getToggle():
							self.click1Music.play()
							self.instructionButton.setToggle(False)
						
						if event.type == pygame.MOUSEBUTTONDOWN:
							self.click2Music.play()
							self.drawStartScreen2()
							self.instructionButton.drawButtonClick()
							pygame.display.update()
							time.sleep(0.6)
														
							self.scene = 2
							self.drawInstruction()
							
							

					elif not self.instructionButton.ifSelected(mousePosition) and self.scene == 0:
						self.instructionButton.drawButton()
						self.instructionButton.setToggle(True)
					
					
					# quit button #
					if self.quitButton.ifSelected(mousePosition) and self.scene == 0:
						self.quitButton.drawButtonFloat()
							
						if self.quitButton.getToggle():
							self.click1Music.play()
							self.quitButton.setToggle(False)
					
						if event.type == pygame.MOUSEBUTTONDOWN:
							self.click2Music.play()
							self.drawStartScreen2()
							self.quitButton.drawButtonClick()
							pygame.display.update()
							time.sleep(0.6)
							
							print "quit the game"
							quit = False

					elif not self.quitButton.ifSelected(mousePosition) and self.scene == 0:
						self.quitButton.drawButton()
						self.quitButton.setToggle(True)
				
				if self.scene == 1:
					self.instructionMusic.stop()
					self.startMusic.stop()
					self.endMusic.stop()
					
					if self.mode == 0:
						self.game2Music.stop()
					elif self.mode == 1:
						self.game1Music.stop()	
					
					if self.mode == 0:
						self.game1Music.play(-1)
					elif self.mode == 1:
						self.game2Music.play(-1)
					



######################################################### decide which card is selected #############################################################
					
					toggle = True

					for i in range(5):

						if self.slot[self.currentUser][i].ifSelected(mousePosition) and self.scene == 1:
							self.slot[self.currentUser][i].draw()
							
							if self.ifUserStart:
								self.slot[self.currentUser][i].getCard().drawBigImage(position = (450, 80))
								toggle = False
							
		
							if event.type == pygame.MOUSEBUTTONDOWN:
								newCard, oldCard = self.slot[self.currentUser][i].deal()
								self.slot[self.currentUser][i].draw()
								cardID = oldCard.getType()	
								selectedTurtle = self.selectTurtle(cardID)
								selectedGrid = self.selectGrid(cardID)
								invalid = self.action(cardID,selectedTurtle,selectedGrid)								
								self.drawGame() 
																
								if invalid:
									self.slot[self.currentUser][i].addCard(oldCard)
									self.deck.addCard(newCard)
								else:

									self.currentUser += 1
									if self.currentUser == 5:
										self.currentUser = 0
									pygame.display.update()
										
									self.oldCard = oldCard
									
									time.sleep(1)
									self.scene = 4
									self.drawPause()
									self.oldCard.drawBigImage(position = (880, 130))
									
						elif not self.slot[self.currentUser][i].ifSelected(mousePosition) and self.scene == 1:	
							self.ifUserStart = True 
							if toggle:
								self.drawGame()
								
							self.slot[self.currentUser][i].drawFloat()
						
			
##########################################################################################################################################

					if self.endButton.ifSelected(mousePosition) and self.scene == 1:
						self.endButton.drawButtonFloat()
						
						if self.endButton.getToggle():
							self.click1Music.play()
							self.endButton.setToggle(False)
						
						if event.type == pygame.MOUSEBUTTONDOWN:
							self.click2Music.play()
							
							self.drawGame2(2)
							self.endButton.drawButtonClick()
							pygame.display.update()
							time.sleep(0.6)
							
							self.players = []
							self.setGame()
							self.drawStartScreen()
							self.scene = 0

					elif not self.endButton.ifSelected(mousePosition) and self.scene == 1:
						self.endButton.drawButton()
						self.endButton.setToggle(True)
						
						
						
					
					if self.informationButton.ifSelected(mousePosition) and self.scene == 1:
						self.informationButton.drawButtonFloat()
						
						for i in range(5):
							text = afont.render( " " + str(self.players[i].getScore()), True, ( 255, 200 - i * 30, 0) )
							self.screen.blit(text, (900, 130 + 75 * i))
							self.players[i].drawPlayerScore((250, 80 + 75 * i))

					elif not self.informationButton.ifSelected(mousePosition) and self.scene == 1:
						self.informationButton.drawButton()							
						
						
						
					
					if self.modeButton.ifSelected(mousePosition) and self.scene == 1:
						self.modeButton.drawButtonFloat()
						
						if event.type == pygame.MOUSEBUTTONDOWN:
							self.click2Music.play()
							
							self.drawGame2(1)
							self.modeButton.drawButtonClick()
							pygame.display.update()
							time.sleep(0.6)
							
							if self.mode == 0:
								self.mode = 1
							elif self.mode == 1:
								self.mode = 0
						

					elif not self.modeButton.ifSelected(mousePosition) and self.scene == 1:
						self.modeButton.drawButton()
						
						
							


					for i in range(5):
						
						if self.players[i].ifSelected(mousePosition) and self.scene == 1:
							
							if self.currentUser == i:
								if self.userOn:
									self.players[self.currentUser].drawPlayerClick()
								
							else:
								self.players[i].drawPlayer()
							
							if event.type == pygame.MOUSEBUTTONDOWN:
								self.ifUserStart = False
								
								if self.currentUser == i:
									self.userOn = True
									self.players[self.currentUser].drawPlayerClick()
									self.currentUser = i+1	
									if self.currentUser == 5:
										self.currentUser = 0	
									time.sleep(1)	
									self.scene = 4
									self.drawPause()
								
						
						elif not self.players[i].ifSelected(mousePosition) and self.scene == 1:
							if self.currentUser == i:
								if self.userOn:
									self.players[self.currentUser].drawPlayerClick2()
							else:
								self.players[i].drawPlayerFloat()

					for i in range(5):
					
						if self.turtles[i].ifSelected(mousePosition) and self.scene == 1:
							self.turtles[i].draw(self.turtles[i].getPosition())
							index = self.players[self.currentUser].getTurtle().getColor()
							if i == index:
								self.turtles[index].drawPhoto(self.turtles[index].getPosition())
								
					if self.peekButton.ifSelected(mousePosition) and self.scene == 1:
						self.peekButton.drawButtonFloat()
						self.drawInstructionWindow((-1, -2))

					elif not self.peekButton.ifSelected(mousePosition) and self.scene == 1:
						self.peekButton.drawButton()



				# Instruction screen #
				if self.scene == 2:
				
					if self.mode == 0:
						self.game1Music.stop()
					elif self.mode == 1:
						self.game2Music.stop()
					
					
					self.startMusic.stop()
					self.endMusic.stop()
					self.instructionMusic.play(-1)
					
					if self.returnButton.ifSelected(mousePosition) and self.scene == 2:
						self.returnButton.drawButtonFloat()
							
						if self.returnButton.getToggle():
							self.click1Music.play()
							self.returnButton.setToggle(False)
						
						if event.type == pygame.MOUSEBUTTONDOWN:
							self.click2Music.play()
							self.drawInstruction2()
							self.returnButton.drawButtonClick()
							pygame.display.update()
							time.sleep(0.6)
							
							self.drawStartScreen()
							self.scene = 0
				
					elif not self.returnButton.ifSelected(mousePosition) and self.scene == 2:
						self.returnButton.drawButton()
						self.returnButton.setToggle(True)


				# Finish scene #
				if self.scene == 3:
					if self.mode == 0:
						self.game1Music.stop()
					elif self.mode == 1:
						self.game2Music.stop()
					
					self.startMusic.stop()
					self.instructionMusic.stop()
					self.endMusic.play(-1)
					
					
					winTurtle = self.grids[9].getTurtle()[0]
					color = winTurtle.getColor()
					
					playerIndex = -1
					for i in range(5):
						if self.players[i].getTurtle().getColor() == color:
							playerIndex = i
					
					if self.players[playerIndex].getScoreToggle():
						self.players[playerIndex].setScore(self.players[playerIndex].getScore() + 1)	
						self.players[playerIndex].setScoreToggle(False)
						
					self.drawFinish(color, playerIndex) 
				
				
					# new button #
					if self.newButton.ifSelected(mousePosition) and self.scene == 3:
						self.newButton.drawButtonFloat()
							
						if self.newButton.getToggle():
							self.click1Music.play()
							self.newButton.setToggle(False)
						
						if event.type == pygame.MOUSEBUTTONDOWN:
							self.click2Music.play()
							
							time.sleep(0.6)
							
							self.setGame()
							self.drawGame()
							self.scene = 1
							self.players[playerIndex].setScoreToggle(True)
									
					elif not self.newButton.ifSelected(mousePosition) and self.scene == 3:
						self.newButton.drawButton()
						self.newButton.setToggle(True)
				
				
				if self.scene == 4:
					if event.type == pygame.KEYDOWN:
							self.drawGame()
							self.scene = 1


				if event.type == pygame.QUIT:
					quit = False
			
#			print self.scene
			pygame.display.update()
	 
		sys.exit()




if __name__ == "__main__":

	turtle = TurtleRace()
	turtle.main()



