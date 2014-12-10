import pygame
from eventManager import EventManager
from static import Static

class Screen():
	"""
	Clase Screen representa una pantalla en donde se pintaran objetos 
	del tipo renderizable ubicados en este mismo paquete de python
	los objetos del tipo screen tendran que ubicar el objeto en un
	numero de capa
	los objetos estaran ubicados por capas, las que se encuentren
	ubicados en la capa de menor numero sera los objetos que se pinten
	primero.
	"""
	
	def __init__(self,tittle,width,height):
		"""
		Esta es la inicializacion de la pantalla a usar.
		@param tittle: el titulo de la ventana
		@param width: el ancho de la ventana
		@param height: el alto de la ventana
		"""
		pygame.init()
		self.__background = (255,255,255)
		self.__yellow = (255,255,0)
		self.__black = (0,0,0)
		self.__blue = (50,50,220)
		self.__open = False
		self.__panel = pygame.Surface((width/3,height))
		self.__eventManager = EventManager(self)
		self.__obstacule = pygame.Rect(500,0,30,480)
		self.__player = Static(pygame.image.load("../images/rocket.png"),0,0)
		self.__screen = pygame.display.set_mode([width,height])
		self.__click = pygame.mixer.Sound("../sound/fredu.ogg")
		pygame.display.set_caption(tittle)
	
	
	def update(self):
		"""
		update: busca la actualizacion realizada en la pantalla
		ademas de buscar los eventos de entrada por el teclado y el mouse,
		ademas de actualizar los objetos renderizables de la ventana
		"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.__open = False
			elif event.type == pygame.KEYDOWN:
				self.__eventManager.keyPressed(event)
			elif event.type == pygame.KEYUP:
				self.__eventManager.keyRelease(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				self.__click.play()
		x = self.__player.getX()
		y = self.__player.getY()
		self.__player.relativeMovement(self.__eventManager.getXMove(),self.__eventManager.getYMove())
		if self.__player.getRect().colliderect(self.__obstacule):
			self.__player.setCoordinate(x,y)
			
	def render(self):
		"""
		render: El metodo render se encarga de pintar las capas de la 
		aplicacion, ademas de utilizar los patrones de disenio cadena de 
		responsabilidades y fabrica para poder realizar el pintado
		"""
		self.__screen.fill(self.__background)
		self.__player.render(self.__screen)
		pygame.draw.rect(self.__screen,self.__blue,self.__obstacule)
		pygame.display.update()

	
	def isOpen(self):
		"""
		isOpen: retorna si la ventana aun sigue abierta o esta cerrada.
		"""
		return self.__open
		
	
	def open(self):
		"""
		open: abre la ventana una sola vez.
		"""
		self.__open = True
	
	
	def close(self):
		"""
		close: la ventana una sola vez.
		"""
		pygame.quit()
