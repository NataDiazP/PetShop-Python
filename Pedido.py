import sys

class Pedido():

	"""
		Pedido: Datos del pedido realizado por el usuario
		Atributos: id, fecha, valorTotal, persona, productos
	"""

	contadorIds = 0

	def __init__(self, fecha, persona, valorTotal = 0, estado="pendiente"):
		Pedido.contadorIds += 1
        self.setId(Pedido.contadorIds)
		self.setFecha(fecha)
		self.setPersona(persona)
		self.setValorTotal(valorTotal)
		self.estado(estado)
		self.setPedidoProductos([])

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

	def setPedidoProductos(self, pedido_productos):
		self._pedido_productos = pedido_productos

	def getPedidoProductos(self):
		return self._pedido_productos

	def crear_pedido(self):
		pass
