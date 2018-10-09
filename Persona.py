import sys

class Persona():

	"""
		Persona: Información básica de usuarios y empleados
		Atributos: id, nombre, email, telefono, direccion, comentarios, pedidos
	"""
	def __init__(self, id, nombre, email, telefono = "", direccion):
		self.setId(id)
		self.setNombre(nombre)
		self.setEmail(email)
		self.setTelefono(telefono)
		self.setDireccion(direccion)
		self.setComentarios([])
		self.setPedidos([])

	def setId(self, id):
		self._id = id

	def getId(self):
		return self._id

	def setNombre(self, nombre):
		self._nombre = nombre

	def getNombre(self):
		return self._nombre

	def setEmail(self, email):
		self._email = email

	def getEmail(self):
		return self._email

	def setTelefono(self, telefono):
		self._telefono = telefono

	def getTelefono(self):
		return self._telefono

	def setDireccion(self, direccion):
		self._direccion = direccion

	def getDireccion(self):
		return self._direccion

	def setComentarios(self, comentarios):
		self._comentarios = comentarios

	def getComentarios(self):
		return self._comentarios

	def setPedidos(self, pedidos):
		self._pedidos = pedidos

	def getPedidos(self):
		return self._pedidos
