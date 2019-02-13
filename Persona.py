class Persona():
    """
    	Persona: Información básica de usuarios y empleados
    	Atributos: id, nombre, email, telefono, direccion, comentarios, pedidos
    """

    contador_ids = 0

    def __init__(self, nombre="", email="", telefono="", direccion="", password=""):
        Persona.contador_ids += 1
        self.setId(Persona.contador_ids)
        self.setNombre(nombre)
        self.setEmail(email)
        self.setTelefono(telefono)
        self.setDireccion(direccion)
        self.setPassword(password)
        self.setListaDeseos([])
        self.setListaCarrito([])
        self.setComentarios([])
        self.setPedidos([])

    def setId(self, id):
        self._id = id

    def getId(self):
        return self._id

    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

    def setEmail(self, email):
        self._email = email

    def getEmail(self):
        return self._email

    def setTelefono(self, telefono):
        self._telefono = telefono

    def getTelefono(self):
        return self._telefono

    def setDireccion(self, direccion):
        self._direccion = direccion

    def getDireccion(self):
        return self._direccion

    def setPassword(self, password):
        self._password = password

    def getPassword(self):
        return self._password

    def setComentarios(self, comentarios):
        self._comentarios = comentarios

    def getComentarios(self):
        return self._comentarios

    def setPedidos(self, pedidos):
        self._pedidos = pedidos

    def getPedidos(self):
        return self._pedidos

    def setListaDeseos(self, listaDeseos):
        self._listaDeseos = listaDeseos

    def getListaDeseos(self):
        return self._listaDeseos

    def setListaCarrito(self, listaCarrito):
        self._listaCarrito = listaCarrito

    def getListaCarrito(self):
        return self._listaCarrito

    def registrarse(self, nombre, email, telefono, direccion, password, lista_personas, mensajes):

        for persona_actual in lista_personas:
            if persona_actual.getEmail() == email:
                return {"exitoso": False,
                        "mensaje": mensajes["error_register"]}

        self.setNombre(nombre)
        self.setEmail(email)
        self.setTelefono(telefono)
        self.setDireccion(direccion)
        self.setPassword(password)

        lista_personas.append(self)

        return {
            "exitoso": True,
            "mensaje": mensajes["succes_register"]
        }

    def iniciar_sesion(self, lista_personas, mensajes):
        for persona_actual in lista_personas:
            if persona_actual.getEmail() == self.getEmail() and persona_actual.getPassword() == self.getPassword():
                self.setId(persona_actual.getId())
                self.setNombre(persona_actual.getNombre())
                self.setTelefono(persona_actual.getTelefono())
                self.setDireccion(persona_actual.getDireccion())
                self.setListaDeseos(persona_actual.getListaDeseos())
                self.setComentarios(persona_actual.getComentarios())
                self.setPedidos(persona_actual.getPedidos())

                return {
                    "exitoso": True,
                    "mensaje": mensajes["succes_login"]
                }

        return {
            "exitoso": False,
            "mensaje": mensajes["error_login"]
        }


    def agregar_lista_deseos(self, producto, mensajes):
        for productoActual in self._listaDeseos:
            if productoActual.getId() == producto.getId():
                return {
                    "exitoso": False,
                    "mensaje": mensajes["product_already_added"]
                }

        self._listaDeseos.append(producto)
        
        return {
            "exitoso": True,
            "mensaje": mensajes["product_added"]
        }

    def agregar_lista_carrito(self, producto, mensajes, cantidadventa):
        for productoActual in self._listaCarrito:
            if productoActual.getId() == producto.getId():
                return {
                    "exitoso": False,
                    "mensaje": mensajes["product_already_added_carrito"]
                }

        self._listaCarrito.append(producto)

        return {
            "exitoso": True,
            "mensaje": mensajes["success_add"]
        }
