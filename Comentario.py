import sys
from Pedido import Pedido

class Comentario():

	"""
		Comentario: Opiniones sobre los productos
		Atributos: id, descripcion, persona, producto
	"""

	contador_ids=0
	def __init__(self, descripcion, persona, producto):
		Comentario.contador_ids+=1

		self.setId(Comentario.contador_ids)
		self.setDescripcion(descripcion)
		self.setPersona(persona)
		self.setProducto(producto)

	def setId(self, id):
		self._id = id

	def getId(self):
		return self._id

	def setDescripcion(self, descripcion):
		self._descripcion = descripcion

	def getDescripcion(self):
		return self._descripcion

	def setPersona(self, persona):
		self._persona = persona
		self._persona.getComentarios().append(self)

	def getPersona(self):
		return self._persona

	def setProducto(self, producto):
		self._producto = producto
		self._producto.getComentarios().append(self)

	def getProducto(self):
		return self._producto

	def toString(self):
		return "\n#"+str(self.getId())+" - "+self.getPersona().getNombre()+ ": " +self.getDescripcion()




