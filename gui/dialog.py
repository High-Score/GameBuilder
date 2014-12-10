import pygame
from renderizable import Renderizable

class Dialog(Rendeizable):
	def __init__(self,text):
		self.__text = text
		self._rec = pygame.Rect(0,0,0,0)
