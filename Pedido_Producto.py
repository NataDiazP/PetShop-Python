class Pedido_Producto():

	"""
		Pedido_Producto: Productos ordenados en un pedido
		Atributos: id, cantidad, subtotal, pedido, producto
	"""

	contador_ids = 0 # Contador de ids - AUTOINCREMENTABLE

	def __init__(self, cantidad, pedido, producto, subtotal = 0):

		"""
			Id: self._id
			Quantity: self._cantidad
			Related order: self._pedido
			Related product: self._producto
			Subtotal Quantity * Product value): self._subtotal
		"""

		Pedido_Producto.contador_ids += 1
		self.setId(Pedido_Producto.contador_ids)
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
		# Devuelve un string con la informacion de los pedidos-producto
		return mensajes["amount"] + str(self.getCantidad()) + mensajes["subtotal"] + str(self.getSubtotal())

	@staticmethod
	def agregarProductoACarritoCompras(cantidad_venta, pedido_pendiente, producto_seleccionado, mensajes):
		# Agrega un producto al carrito de compras

		# Esta parte de aqui se encarga de actualizar en caso de que ya exista el producto en el pedido de compras y si existe le actualiza la cantidad de compra con la que nueva que se ingreso
		for item_carrito in pedido_pendiente.getPedidoProductos():
			if item_carrito.getProducto().getId() == producto_seleccionado.getId():
				# Se valida si la cantidad del producto en el inventario es suficiente para la cantidad que se desea comprar
				if item_carrito.getProducto().validarCantidadInventario(cantidad_venta):
					item_carrito.setCantidad(cantidad_venta)

					# Se actualiza el subtotal en ese pedido_ producto y el total del pedido se recalcula con la nueva cantidad a comprar
					item_carrito.setSubtotal(cantidad_venta * producto_seleccionado.getValor())
					pedido_pendiente.calcularValorTotal()

					return {
						"exitoso": True,
						"mensaje": mensajes["success_cart_add"]
					}

				else:
					return {
						"exitoso": False,
						"mensaje": mensajes["product_sold_out"] + item_carrito.getProducto().getCantidadInventario()
					}

		# Si el producto no se ha encontrado en el carrito de compras, se verifica si hay cantidad suficiente en inventario y se agrega un nuevo pedido_producto al pedido actual.
		if producto_seleccionado.validarCantidadInventario(cantidad_venta):
			Pedido_Producto(cantidad_venta, pedido_pendiente, producto_seleccionado)
			pedido_pendiente.calcularValorTotal()

			return {
				"exitoso": True,
				"mensaje": mensajes["success_cart_add"]
			}
		else:
			return {
				"exitoso": False,
				"mensaje": mensajes["product_sold_out"] + str(producto_seleccionado.getCantidadInventario())
			}

	@staticmethod
	def borrarProductoDeCarritoCompras(id_producto, pedido_pendiente, mensajes):
		# Borra el producto del carrito de compras
		for item_carrito in pedido_pendiente.getPedidoProductos():
			if item_carrito.getProducto().getId() == id_producto:
				pedido_pendiente.getPedidoProductos().remove(item_carrito)
				pedido_pendiente.calcularValorTotal()
				
				return mensajes["product_deleted"]

		return mensajes["product_not_found"]
