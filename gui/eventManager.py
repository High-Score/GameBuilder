import pygame

class EventManager():
	
	def __init__(self, pScreen):
		self.__screen = pScreen
		self.__yMove = 0
		self.__xMove = 0
		self.__yNextMovement = 0
		self.__xNextMovement = 0
	
	def keyPressed(self,event):
		if event.key == pygame.K_UP:
			if self.__yMove == 0:
				self.__yMove = -10
				self.__yNextMovement = 0
			else:
				self.__yNextMovement = -10
		elif event.key == pygame.K_DOWN:
			if self.__yMove == 0:
				self.__yMove = 10
				self.__yNextMovement = 0
			else:
				self.__yNextMovement = 10
		elif event.key == pygame.K_LEFT:
			if self.__xMove == 0:
				self.__xMove = -10
				self.__xNextMovement = 0
			else:
				self.__xNextMovement = -10
		elif event.key == pygame.K_RIGHT:
			if self.__xMove == 0:
				self.__xMove = 10
				self.__xNextMovement = 0
			else:
				self.__xNextMovement = 10
	
	def keyRelease(self,event):
		if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
			self.__yMove = self.__yNextMovement
			self.__yNextMovement = 0
		if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
			self.__xMove = self.__xNextMovement
			self.__xNextMovement = 0
	def mouseListener(self,event):
		print("hello")
	def getYMove(self):
		return self.__yMove
	def getXMove(self):
		return self.__xMove
	def getYNextMovement(self):
		return self.__yNextMovement
	def getXNextMovement(self):
		return self.__xNextMovement
