import sys

from Persona import Persona

class Empleado(Persona):
    """
        Empleado: Información de los trabajadores
        Atributos: admin, productos, pedidosAnulados
    """

    def __init__(self, nombre="", email="", password="", telefono="", direccion="", admin=False, activo=True):
        super().__init__(nombre, email, telefono, direccion, password)
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
                if empleado.getActivo() == False:
                    return {
                        "exitoso": False,
                        "mensaje": mensajes["deactivated_employee"]
                    }

                self.setId(empleado.getId())
                self.setNombre(empleado.getNombre())
                self.setTelefono(empleado.getTelefono())
                self.setDireccion(empleado.getDireccion())
                self.setAdmin(empleado.getAdmin())
                self.setActivo(empleado.getActivo())
                self.setProductos(empleado.getProductos())
                self.setPedidosAnulados(empleado.getPedidosAnulados())

                return {
                    "exitoso": True,
                    "mensaje": mensajes["succes_login"]
                }

        return {
            "exitoso": False,
            "mensaje": mensajes["error_login"]
        }

    def crearEmpleado(self, empleados, mensajes):
        archivo = open("empleados.txt","r")

        for linea in archivo:
            if linea.split(";")[1] == self.getEmail():
                archivo.close()
                
                return {
                    "exitoso": False,
                    "mensaje": mensaje["error_register"]
                }

        archivo = open("empleados.txt","a")
        archivo.write(self.getNombre() + ";" + self.getEmail() + ";" + self.getPassword() + ";" + self.getTelefono() + ";" + self.getDireccion() + ";"+ str(self.getAdmin()) + ";" + str(self.getActivo()) + "\n")
        archivo.close()

        empleados.append(self)

        return {
            "exitoso": True,
            "mensaje": mensajes["empl_added"]
        }

    def listarEmpleado(self, mensajes):
        return mensajes["user_id"] + str(self.getId()) + mensajes["user_name"] + self.getNombre() + mensajes["email"] + self.getEmail() + mensajes["user_phone"] + self.getTelefono() + mensajes["user_address"] + self.getDireccion() + mensajes["user_active"] + self.getActivo()

    @staticmethod
    def cambiarEstadoEmpleado(id_empleado, empleados, mensajes):
        for empleado in empleados:
            if empleado.getId() == id_empleado:
                estado_actual = empleado.getActivo()
                empleado.setActivo(not estado_actual)

        return {
            "mensaje": (mensajes["deactivate_confirmation"] if estado_actual else mensajes["activate_confirmation"])
        }


    # def EliminarEmpleado(self, empleadosList, mensajes):
