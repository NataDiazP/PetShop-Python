from Persona import Persona

class Empleado(Persona):

    """
        Empleado: Información de los trabajadores
        Atributos: _admin, _activo
    """

    empleados = [] # Lista de empleados

    def __init__(self, nombre="", email="", password="", telefono="", direccion="", admin=False, activo=True):

        """
            Id: self._id
            Name: self._nombre
            Email: self._email
            Telephone: self._telefono
            Address: self._direccion
            Password: self._password
            Admin (True-False): self._admin
            Active (True-False): self._activo
        """

        super().__init__(nombre, email, telefono, direccion, password)
        self.setAdmin(admin)
        self.setActivo(activo)

    def setAdmin(self, admin):
        self._admin = admin

    def getAdmin(self):
        return self._admin

    def setActivo(self, activo):
        self._activo = activo

    def getActivo(self):
        return self._activo

    def iniciar_sesion(self, mensajes):
        # Metodo que sirve para iniciar sesion desde empleado
        for empleado in Empleado.empleados:
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

                return {
                    "exitoso": True,
                    "mensaje": mensajes["succes_login"]
                }

        return {
            "exitoso": False,
            "mensaje": mensajes["error_login"]
        }

    def guardarEmpleadoTxt(self, mensajes):
        # Metodo que sirve para guardar un empleado en el archivo txt "empleados.txt"
        archivo = open("empleados.txt","r")

        for linea in archivo:
            # Al partir la linea por ;, en la segunda posicion de esa lista que nos devuelve tendriamos el email
            if linea.split(";")[1] == self.getEmail():
                archivo.close()

                return {
                    "exitoso": False,
                    "mensaje": mensajes["error_register"]
                }
        # Se abre el archivo en modo append para agregar al final de ese archivo un nuevo empleado
        archivo = open("empleados.txt","a")
        archivo.write(self.getNombre() + ";" + self.getEmail() + ";" + self.getPassword() + ";" + self.getTelefono() + ";" + self.getDireccion() + ";"+ str(self.getAdmin()) + ";" + str(self.getActivo()) + "\n")
        archivo.close()

        Empleado.empleados.append(self)

        return {
            "exitoso": True,
            "mensaje": mensajes["empl_added"]
        }

    def toString(self, mensajes):
        return mensajes["user_id"] + str(self.getId()) + mensajes["user_name"] + self.getNombre() + mensajes["email"] + self.getEmail() + mensajes["user_phone"] + self.getTelefono() + mensajes["user_address"] + self.getDireccion() + mensajes["user_active"] + str(self.getActivo())

    @staticmethod
    # Metodo que sirve para cambiar el estado del empleado entre activado y desactivado
    def cambiarEstadoEmpleado(id_empleado, mensajes):
        for empleado in Empleado.empleados:
            if empleado.getId() == id_empleado:
                estado_actual = empleado.getActivo()
                empleado.setActivo(not estado_actual)

                return {
                    "mensaje": (mensajes["deactivate_confirmation"] if estado_actual else mensajes["activate_confirmation"])
                }

        return {
            "mensaje": mensajes["employee_not_found"]
        }
