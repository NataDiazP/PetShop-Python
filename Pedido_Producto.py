import sys

class Pedido_Producto():

	"""
		Pedido_Producto: Productos ordenados en un pedido
		Atributos: id, cantidad, subtotal, pedido, producto
	"""

	contadorIds = 0

	def __init__(self, cantidad, pedido, producto, subtotal = 0):
		Pedido_Producto.contadorIds += 1
        self.setId(Pedido_Producto.contadorIds)
		self.setCantidad(cantidad)
		self.setPedido(pedido)
		self.setProducto(producto)
		self.setSubtotal(subtotal)

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
		self._pedido.getPedidoProductos().append(self)

	def getPedido(self):
		return self._pedido

	def setProducto(self, producto):
		self._producto = producto
		self._producto.getPedidosProducto().append(self)

	def getProducto(self):
		return self._producto
