from abc import ABCMeta, abstractmethod

class Renderizable(object):
	"""
	Clase Renderizable. Esta clase es la que encapsula a las demas para que pueda
	pintarse en el lienzo o la pantalla, las clases hijas de Renderizable, saben pintarse
	en el lienzo que se les pasa por el metodo 
	:link Renderizable#render(self):.
	"""
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def render(self,canvas):
		"""
		Render. Pinta su contenido en el parametro canvas, este metodo esta sujeto 
		a las clases hijas, quienes implementaran por si mismas la forma de pintarse.
		:param canvas: Es el lienzo en donde se pintaran los objetos asociados.
		:type cavas: el tipo de cavas pertenece a 
		:link pygame.Surface:.
		"""
		pass
	@abstractmethod
	def update(self):
		"""
		Update. Actualiza la clase ya sea en coordenadas, fisica de colisiones o de grevedad,
		o actualizacion de sprites.
		"""
		pass
	def setX(self,x):
		"""
		SetX. Actualiza la coordenada en el eje x en donde este se pinte.
		:param x: 
		"""
		self._rec.x = x
	
	def setY(self,y):
		"""
		SetY. Actualiza la coordenada en el eje y en donde este se pinte.
		:param y:
		"""
		self._rec.y = y
	
	def getX(self):
		"""
		GetX. Obtiene la coordenada x.
		:return: la coordenada en el eje x, representada por un numero entero
		"""
		return self._rec.x
	
	def getY(self):
		"""
		GetY. Obtiene la coordenada en el eje y.
		:return: la coordenada en el eje y, representada por un numero entero
		"""
		return self._rec.y
	
	def getWidth(self):
		"""
		GetWidth. Obtiene el ancho del objeto renderizable, representada por un numero entero.
		:return:  el ancho del objeto renderizable
		"""
		return self._rec.w
	
	def getHeight(self):
		"""
		GetHeight. Obtiene el alto del objeto renderizable, representada por un numero entero.
		:return: el alto del objeto renderizable
		"""
		return self._rec.h
		
	def relativeMovement(self,x,y):
		"""
		RelativeMovement. Mueve relativamente el objeto, las coordanas actuales
		mas las coordenadas dadas por los parametros.
		:param x: lo que se movera el objeto en el eje x, para la izquierda un numero
		negativo, para la derecha un numero positivo y en caso de no mover un 0.
		:type x: int
		:param y:lo que se movera el objeto en el eje y, para arriba un numero
		negativo, para abajo un numero positivo y en caso de no mover un 0.
		:type y: int
		"""
		self._rec.move_ip(x,y)
		
	def getRect(self):
		"""
		getRect. Obtiene el rectangulo asociado al objeto hijo de la clase Renderizable
		:return: el rectangulo asociado al objeto.
		"""
		return self._rec
	
	def setCoordinate(self,x,y):
		"""
		setCoordinate. Actualiza las coordanas `x` y `y` a las coordenadas deseadas.
		:param x: la nueva coordenada en el eje x
		:type x: int 
		:param y:la nueva coordenada en el eje y
		:type y: int
		"""
		self.setX(x)
		self.setY(y)
	
	def isCollide(self,otherRendezable):
		"""
		IsCollide. Verifica si este objeto esta colisionando con otro objeto.
		:param otherRendezable: el otro objeto.
		:type otherRendezable: Renderizable
		:return: True, si el objeto esta colisionando con el obejeto otherRendezable.
		en caso contrario retorna False.
		
		"""
		return self._rec.colliderect(otherRendezable.getRect())

