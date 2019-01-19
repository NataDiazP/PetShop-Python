
class Pedido():

	```
		Pedido: Datos del pedido realizado por el usuario
		Atributos: id, fecha, valorTotal, empleadoAnulador, persona, productos
	```
	def __init__(self, id, fecha, valorTotal, empleadoAnulador, persona, productos):
		self.setId(id)
		self.setFecha(fecha)
		self.setValorTotal(valorTotal)
		self.setEmpleadoAnulador(empleadoAnulador)
		self.setDireccion(direccion)
		self.setComentarios([])
		self.setPedidos([])

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

	def setEmpleadoAnulador(self, empleadoAnulador):
		self._empleadoAnulador = empleadoAnulador
		self._empleadoAnulador.getPedidosAnulados().append(self)

	def getEmpleadoAnulador(self):
		return self._empleadoAnulador

FALTAN OTROS
