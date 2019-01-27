import sys


class Persona():
    """
    	Persona: Información básica de usuarios y empleados
    	Atributos: id, nombre, email, telefono, direccion, comentarios, pedidos
    """

    lista_personas = []

    def __init__(self, id=0, nombre="", email="", telefono="", direccion="", password=""):
        self.setId(id)
        self.setNombre(nombre)
        self.setEmail(email)
        self.setTelefono(telefono)
        self.setDireccion(direccion)
        self.setPassword(password)
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

    def getPassoword(self):
        return self._password

    def setComentarios(self, comentarios):
        self._comentarios = comentarios

    def getComentarios(self):
        return self._comentarios

    def setPedidos(self, pedidos):
        self._pedidos = pedidos

    def getPedidos(self):
        return self._pedidos

    def registrarse(self, nombre, email, telefono, direccion, password):

        archivo = open("usuarios.txt", "r")
        usuario_existe = 0

        for linea in archivo:

            if linea.split(";")[0] == email:
                archivo.close()
                usuario_existe = 1
                break

        if usuario_existe == 0:

            self.setNombre(nombre)
            self.setEmail(email)
            self.setTelefono(telefono)
            self.setDireccion(direccion)
            self.setPassword(password)

            archivo = open("usuarios.txt", "a")
            archivo.write(email + ";" + password + ";" + nombre + ";" + direccion + ";" + telefono + "\n")
            archivo.close()

            self.lista_personas.append(self)
            return True

        else:

            return False


    def iniciar_sesion(self, email, password):

        archivo = open("usuarios.txt", "r")
        usuario_existe = 0

        for linea in archivo:

            if linea.split(";")[0] == email:

                if linea.split(";")[1] == password:

                    archivo.close()

                    datos = linea.split(";")
                    self.setEmail(datos[0])
                    self.setPassword(datos[1])
                    self.setNombre(datos[2])
                    self.setDireccion(datos[3])
                    self.setTelefono(datos[4])
                    usuario_existe = 1
                    break

        if usuario_existe == 0:

            return False

        else:

            return True

