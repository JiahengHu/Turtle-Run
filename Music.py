# Liwei Jiang, Yin Li, Kebing Li
# CS269 JP17
# Computer Game Design
# Music.py
# Jan. 17th 2017

import pygame

class Music:
	
	def __init__(self, channel, music ):
		self.music = None
		self.toggle = True
		self.first = True
		self.channel = channel
		self.setMusic(music)

	def setToggle(self, toggle):
		self.on = toggle

	def getToggle(self):
		return self.toggle

	def setMusic(self, music):
		self.music = pygame.mixer.Sound(music)

	def getMusic(self):
		return self.music

	def play(self, time = 0):
		if self.toggle:
			self.channel.play(self.music, time)
			self.toggle = False
			if self.first:
				self.first = False

	def stop(self):
		
		if not self.first:
			if not self.toggle:
				self.channel.stop()
				self.toggle = True


