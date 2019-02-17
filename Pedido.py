from Producto import Producto
import datetime

class Pedido():

	"""
		Pedido: Datos del pedido realizado por el usuario
		Atributos: id, fecha, valorTotal, persona, pedido_productos, estado
	"""

	pedidos = []
	contadorIds = 0

	def __init__(self, fecha, persona, valorTotal = 0, estado="Pendiente"):
		"""
			Id: self._id
			Fecha: self._fecha
			Valor Total: self._valorTotal
			Persona: self._persona
			Estado: self._estado
		"""

		Pedido.contadorIds += 1
		Pedido.pedidos.append(self)
		self.setId(Pedido.contadorIds)
		self.setFecha(fecha)
		self.setPersona(persona)
		self.setValorTotal(valorTotal)
		self.setEstado(estado)
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

	def setEstado(self, estado):
		self._estado = estado

	def getEstado(self):
		return self._estado

	def setPedidoProductos(self, pedido_productos):
		self._pedido_productos = pedido_productos

	def getPedidoProductos(self):
		return self._pedido_productos

	def comprar(self, total):
		for pedido_producto in self.getPedidoProductos():
			producto_seleccionado = pedido_producto.getProducto()
			producto_seleccionado.setCantidadInventario(producto_seleccionado.getCantidadInventario() - pedido_producto.getCantidad())

		self.setFecha(datetime.date.today())
		self.setValorTotal(total)
		self.setEstado("Realizado")

	@staticmethod
	def anularPedido(id_pedido, mensajes):
		for pedido_actual in Pedido.pedidos:
			if pedido_actual.getId() == id_pedido:
				for pedido_producto in pedido_actual.getPedidoProductos():
					producto_seleccionado = pedido_producto.getProducto()
					producto_seleccionado.setCantidadInventario(producto_seleccionado.getCantidadInventario() + pedido_producto.getCantidad())

				pedido_actual.setEstado("Anulado")
				return mensajes["order_successfully_cancel"]
		return mensajes["order_to_cancel_not_found"]
