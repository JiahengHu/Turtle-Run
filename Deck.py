# Liwei Jiang, Yin Li, Kebing Li
# CS269 JP17
# Computer Game Design
# Deck.py
# Jan. 15th 2017

import random
from Card import Card

class Deck:

	def __init__(self, screen):
		self.deck = []
		self.screen = screen
		self.build()
		self.shuffle()

	def getDeck(self):
		return self.deck
   
	def build(self):
		for j in range(1):
			for i in [1,2]:
				card = Card(self.screen,i)
				self.deck.append(card)
		for j in range(5):
			for i in range(4,24):
				if i%4 == 0 or i%4 == 1:
					card = Card(self.screen, i)
					self.deck.append(card)
					
 		for j in range(2):
 			
 			for i in range(4,24):
 				if i%4 == 2 or i%4 == 3:
 					card = Card(self.screen, i)
 					self.deck.append(card)
 
 		for j in range(1):
 			
 			for i in range(24,28):
 				card = Card(self.screen, i)
 				self.deck.append(card)


 		for j in range(1):	
 			for i in [29,30,31,32,33,34,35,36,40,41]:
 				card = Card(self.screen, i)
 				self.deck.append(card)

	def deal(self):
		top = self.deck.pop()
		if len(self.deck) <= 0:
			self.build()
			self.shuffle()
		return top
	
	def addCard(self, card):
		self.deck.insert(0, card)
	
	def shuffle(self):
		random.shuffle(self.deck)
		
	def printContent(self):
		for i in range(len(self.deck)):
			print self.deck[i].getTag()

if __name__ == "__main__":
	deck = Deck(12)
	size = len(deck.getDeck())
	for i in range(size+12):
		deck.deal()
	
	deck.printContent()
	size = len(deck.getDeck())
	print size


