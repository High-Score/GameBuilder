from renderizable import Renderizable

class Static(Renderizable):
	"""
	
	"""
	def __init__(self,img,x,y):
		"""
		
		@param img: la imagen que asociada al objeto estatico
		@type img: pygame.image 
		@param x: la posicion en el eje x
		@type x: int 
		@param y: la posicion en el eje y
		@type x: int 
		"""
		self.__img = img
		self._rec = img.get_rect()
		self.setX(x)
		self.setY(y)
	def render(self,canvas):
		"""
		
		@param canvas: es el lugar en el que se pinta el objeto estatico
		@type canvas: pygame.Surface
		"""
		canvas.blit(self.__img,(self._rec.x,self._rec.y))
	def update(self):
		"""
		
		"""
		print("update")
