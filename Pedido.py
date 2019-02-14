import sys

class Pedido():

	"""
		Pedido: Datos del pedido realizado por el usuario
		Atributos: id, fecha, valorTotal, persona, productos
	"""
	def __init__(self, fecha, persona, valorTotal = 0):
		self.setId(id)
		self.setFecha(fecha)
		self.setValorTotal(valorTotal)
		self.setPersona(persona)
		self.setProductos([])

	def setId(self, id):
		self._id = id

	def getId(self):
		return self._id

	def setFecha(self, fecha):
		self._fecha = fecha

	def getFecha(self):
		return self._fecha

	def setValorTotal(self, valorTotal):
		self._valorTotal = valorTotal

	def getValorTotal(self):
		return self._valorTotal

	def setPersona(self, persona):
		self._persona = persona
		self._persona.getPedidos().append(self)

	def getPersona(self):
		return self._persona

	def setProductos(self, productos):
		self._productos = productos

	def getProductos(self):
		return self._productos

	def crear_pedido(self):
		pass
