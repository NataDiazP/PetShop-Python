import sys

class Pedido_Producto():

	"""
		Pedido_Producto: Productos ordenados en un pedido
		Atributos: id, cantidad, subtotal, pedido, producto
	"""
	def __init__(self, cantidad, pedido, producto, subtotal = 0):
		self.setId(id)
		self.setCantidad(cantidad)
		self.setSubtotal(subtotal)
		self.setPedido(pedido)
		self.setProducto(producto)

	def setId(self, id):
		self._id = id

	def getId(self):
		return self._id

	def setCantidad(self, cantidad):
		self._cantidad = cantidad

	def getCantidad(self):
		return self._cantidad

	def setSubtotal(self, subtotal):
		self._subtotal = subtotal

	def getSubtotal(self):
		return self._subtotal

	def setPedido(self, pedido):
		self._pedido = pedido
		self._pedido.getProductos().append(self)

	def getPedido(self):
		return self._pedido

	def setProducto(self, producto):
		self._producto = producto
		self._producto.getPedidos().append(self)

	def getProducto(self):
		return self._producto
