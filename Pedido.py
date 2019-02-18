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
		self.setId(Pedido.contadorIds)
		self.setFecha(fecha)
		self.setPersona(persona)
		self.setValorTotal(valorTotal)
		self.setEstado(estado)
		self.setPedidoProductos([])

		Pedido.pedidos.append(self)

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

	def toString(self, mensajes):
		resumen_pedido = "------------------------------------------"

		resumen_pedido += "\n"+mensajes["order_number"] + str(self.getId()) + mensajes["state"] + self.getEstado() + mensajes["date"] + str(
			self.getFecha()) + mensajes["order_total_value"] + str(self.getValorTotal()) + mensajes["details"]

		for pedido_producto in self._pedido_productos:
			producto_seleccionado = pedido_producto.getProducto()
			resumen_pedido += "\n\n" + producto_seleccionado.toStringCarrito(mensajes) + pedido_producto.toString(mensajes)

		resumen_pedido += "\n------------------------------------------"

		return resumen_pedido

	def toStringProductosCarrito(self, mensajes):
		resumen_pedido = ""

		for pedido_producto in self._pedido_productos:
			producto_seleccionado = pedido_producto.getProducto()
			resumen_pedido += "------------------------------------------\n"
			resumen_pedido += producto_seleccionado.toStringCarrito(mensajes) + pedido_producto.toString(mensajes)
			resumen_pedido += "\n------------------------------------------\n"

		resumen_pedido += "------------------------------------------"
		resumen_pedido += mensajes["order_total_value"] + str(self.getValorTotal())
		resumen_pedido += "\n------------------------------------------"

		return resumen_pedido

	def calcularValorTotal(self):
		valor_total = 0

		for pedido_producto in self._pedido_productos:
			valor_total += pedido_producto.getSubtotal()

		self.setValorTotal(valor_total)

	def comprar(self):
		for pedido_producto in self.getPedidoProductos():
			producto_seleccionado = pedido_producto.getProducto()
			producto_seleccionado.setCantidadInventario(producto_seleccionado.getCantidadInventario() - pedido_producto.getCantidad())

		self.setFecha(datetime.date.today())
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
