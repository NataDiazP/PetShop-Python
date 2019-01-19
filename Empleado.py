from Persona import Persona

class Empleado(Persona):

	```
		Empleado: Información de los trabajadores
		Atributos: admin, productos, pedidosAnulados
	```
	def __init__(self, id, nombre, email, telefono, direccion, admin):
		super().__init__(id, nombre, email, telefono, direccion)
		self.setAdmin(admin)
		self.setProductos([])
		self.setPedidosAnulados([])

	def setAdmin(self, admin):
		self._admin = admin

	def getAdmin(self):
		return self._admin

	def setProductos(self, productos):
		self._productos = productos

	def getProductos(self):
		return self._productos

	def setPedidosAnulados(self, pedidosAnulados):
		self._pedidosAnulados = pedidosAnulados

	def getPedidosAnulados(self):
		return self._pedidosAnulados
