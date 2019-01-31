import sys

from Persona import Persona

class Empleado(Persona):

    """
        Empleado: Información de los trabajadores
        Atributos: admin, productos, pedidosAnulados
    """
    def __init__(self, id=0, nombre="", email="", password="", telefono="", direccion="", admin=False, activo=True):
        super().__init__(id, nombre, email, telefono, direccion)
        self.setAdmin(admin)
        self.setActivo(activo)
        self.setProductos([])
        self.setPedidosAnulados([])

    def setAdmin(self, admin):
        self._admin = admin

    def getAdmin(self):
        return self._admin

    def setActivo(self, activo):
        self._activo = activo

    def getActivo(self):
        return self._activo

    def setProductos(self, productos):
        self._productos = productos

    def getProductos(self):
        return self._productos

    def setPedidosAnulados(self, pedidosAnulados):
        self._pedidosAnulados = pedidosAnulados

    def getPedidosAnulados(self):
       return self._pedidosAnulados

    def iniciar_sesion(self, empleados, mensajes):
        for empleado in empleados:
            if empleado.getEmail() == self.getEmail() and empleado.getPassword() == self.getPassword():
                    return {
                        "exitoso": False,
                        "mensaje": mensajes["error_login"],
                        "datos": empleado
                    }

        return {
            "exitoso": True,
            "mensaje": mensajes["succes_login"],
            "datos": empleado
        }

    def crearEmpleado(self, empleadosList, mensajes):
        # Esto debe ser guardado en un txt
    	for empl in empleadosList:
    		if(empl.getEmail() == self.getEmail()):
    			return {
    				exitoso: False,
    				mensaje: mensajes["empl_exists"]
    			}

    	empleadosList.append(self)	

    	return {
    		exitoso: True,
    		mensaje: mensajes["empl_added"],
    		data: empleadosList
    	}

    # def EliminarEmpleado(self, empleadosList, mensajes):