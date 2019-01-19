import sys

class Comentario():

	"""
		Comentario: Opiniones sobre los productos
		Atributos: id, descripcion, persona, producto
	"""
	def __init__(self, id, descripcion, persona, producto):
		self.setId(id)
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
