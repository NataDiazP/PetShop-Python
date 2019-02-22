import datetime

class Pedido():

	"""
		Pedido: Datos del pedido realizado por el usuario
		Atributos: id, fecha, valorTotal, persona, pedido_productos, estado
	"""

	pedidos = [] # Lista de pedidos
	contador_ids = 0 # Contador de ids - AUTOINCREMENTABLE

	def __init__(self, fecha, persona, valorTotal = 0, estado="Pendiente"):

		"""
			Id: self._id
			Date: self._fecha
			Value Total: self._valorTotal
			Related person: self._persona
			State: self._estado
		"""

		Pedido.contador_ids += 1
		self.setId(Pedido.contador_ids)
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
		resumen_pedido = "-------------------------------------------------"

		resumen_pedido += "\n" + mensajes["order_number"] + str(self.getId()) + mensajes["state"] + self.getEstado() + mensajes["date"] + str(
			self.getFecha()) + mensajes["order_total_value"] + str(self.getValorTotal()) + mensajes["details"]

		for pedido_producto in self._pedido_productos:
			producto_seleccionado = pedido_producto.getProducto()
			resumen_pedido += "\n\n" + producto_seleccionado.toStringCarrito(mensajes) + pedido_producto.toString(mensajes)

		resumen_pedido += "\n-------------------------------------------------"

		return resumen_pedido

	def toStringProductosCarrito(self, mensajes):
		resumen_pedido = ""

		for pedido_producto in self._pedido_productos:
			producto_seleccionado = pedido_producto.getProducto()
			resumen_pedido += "\n-------------------------------------------------\n"
			resumen_pedido += producto_seleccionado.toStringCarrito(mensajes) + pedido_producto.toString(mensajes)
			resumen_pedido += "\n-------------------------------------------------\n"

		resumen_pedido += "\n-------------------------------------------------"
		resumen_pedido += mensajes["order_total_value"] + str(self.getValorTotal())
		resumen_pedido += "\n-------------------------------------------------"

		return resumen_pedido

	def calcularValorTotal(self):
        # Metodo que sirve para calcular el valor total de un pedido sumando todos los subtotales de sus pedido_producto
		valor_total = 0

		for pedido_producto in self._pedido_productos:
			valor_total += pedido_producto.getSubtotal()

		self.setValorTotal(valor_total)

	def comprar(self):
        # Metodo que sirve para comprar determinado pedido y descontar del inventario las unidades de cada producto que tenga este pedido
		for pedido_producto in self.getPedidoProductos():
			producto_seleccionado = pedido_producto.getProducto()
			producto_seleccionado.setCantidadInventario(producto_seleccionado.getCantidadInventario() - pedido_producto.getCantidad())

		self.setFecha(datetime.date.today())
		self.setEstado("Realizado")

	@staticmethod
	def anularPedido(id_pedido, mensajes):
        # Metodo que sirve para anular un pedido desde la clase empleado
		for pedido_actual in Pedido.pedidos:
			if pedido_actual.getId() == id_pedido:
				for pedido_producto in pedido_actual.getPedidoProductos():
					producto_seleccionado = pedido_producto.getProducto()
					# Al anular pedido devemos devolver las unidades que se habian "comprado" al inventario
					producto_seleccionado.setCantidadInventario(producto_seleccionado.getCantidadInventario() + pedido_producto.getCantidad())

				pedido_actual.setEstado("Anulado")
				return mensajes["order_successfully_cancel"]
		return mensajes["order_to_cancel_not_found"]

	@staticmethod
	def productosAcomentar(usuario_actual):
        # Metodo que sirve para encontrar los productos comprados desde todos los pedidos realizados por una persona, devuelve una lista con todos los productos comprados sin repetir
		lista_productos_a_comentar = []
		producto_agregado = False

		for pedido_actual in Pedido.pedidos:
			if pedido_actual.getEstado()=="Realizado" and pedido_actual.getPersona() == usuario_actual:
				for pedido_producto in pedido_actual.getPedidoProductos():
					producto_actual = pedido_producto.getProducto()

					# Comprobamos si el producto ya se agrego a la lista de productos de comentar para no agregarlo nuevamente
					for prod in lista_productos_a_comentar:
						if prod.getId() == producto_actual.getId():
							producto_agregado = True
							break

					if producto_agregado == False:
						lista_productos_a_comentar.append(producto_actual)
					else:
						producto_agregado = False

		return lista_productos_a_comentar

	@staticmethod
	def valorPromedioYTotalVentasDia():
        # Metodo que sirve para calcular el promedio y el total de las ventas en el dia
		valor_total_dia = 0
		contador = 0

		for pedido_actual in Pedido.pedidos:
			if pedido_actual.getFecha() == datetime.date.today():
				valor_total_dia += pedido_actual.getValorTotal()
				contador += 1

		if contador > 0:
			return {
				"promedio": (valor_total_dia / contador),
				"total": valor_total_dia
			}
		else:
			return {
				"promedio": 0,
				"total": 0
			}
