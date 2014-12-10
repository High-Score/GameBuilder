import pygame
from renderizable import Renderizable

class Animation(Renderizable):
	def __init__(self, r):
		self._rec = r
	def __init__(self,x,y,h,w):
		self._rec = pygame.Rect(x,y,w,h)
