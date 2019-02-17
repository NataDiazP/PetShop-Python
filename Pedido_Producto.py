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
		self.setSubtotal(cantidad * producto.getValor())

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

	def toString(self, mensajes):
		return mensajes["amount"]+str(self.getCantidad())+mensajes["subtotal"]+str(self.getSubtotal())

	@staticmethod
	def agregarProductoACarritoCompras(cantidad_venta, pedido_pendiente, producto_seleccionado, usuario_actual, mensajes):
		for item_carrito in pedido_pendiente.getPedidoProductos():
			if item_carrito.getProducto().getId() == producto_seleccionado.getId():
				if item_carrito.getProducto().validarCantidadInventario(cantidad_venta):
					item_carrito.setCantidad(cantidad_venta)
					item_carrito.setSubtotal(cantidad_venta * producto_seleccionado.getValor())

					return {
						"exitoso": True,
						"mensaje": mensajes["success_cart_add"]
					}

				else:
					return {
						"exitoso": False,
						"mensaje": mensajes["product_sold_out"] + item_carrito.getProducto().getCantidadInventario()
					}

		if producto_seleccionado.validarCantidadInventario(cantidad_venta):
			Pedido_Producto(cantidad_venta, pedido_pendiente, producto_seleccionado)
            # usuario_actual.actualizarCarrito(Main.pedido_pendiente)

			return {
				"exitoso": True,
				"mensaje": mensajes["success_cart_add"]
			}
		else: 
			return {
				"exitoso": False,
				"mensaje": mensajes["product_sold_out"] + str(producto_seleccionado.getCantidadInventario())
			}



