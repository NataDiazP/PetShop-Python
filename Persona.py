import sys

class Persona():
    
    """
    	Persona: Información básica de usuarios y empleados
    	Atributos: id, nombre, email, telefono, direccion, comentarios, pedidos
    """

    def __init__(self, id="", nombre="", email="", telefono="", direccion=""):
        self.setId(id)
        self.setNombre(nombre)
        self.setEmail(email)
        self.setTelefono(telefono)
        self.setDireccion(direccion)
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

    def setComentarios(self, comentarios):
        self._comentarios = comentarios

    def getComentarios(self):
        return self._comentarios

    def setPedidos(self, pedidos):
        self._pedidos = pedidos

    def getPedidos(self):
        return self._pedidos

    def registrarse(self):

        registro_terminado = 0

        while registro_terminado == 0:

            usuario = input("\nIngrese un nombre de usuario para su cuenta: ")
            usuario_existe = 0
            archivo = open("usuarios.txt","r")

            for linea in archivo:

                    if linea.split(";")[0] == usuario:

                            print("\nAlguien ya ha tomado ese nombre de usuario, por favor selecciona otro.")
                            archivo.close()
                            usuario_existe = 1
                            break

            if usuario_existe == 0:

                    print("\nA continuacion se le pediran algunas datos personales para terminar con el registro de su cuenta.")

                    nombre = input("\n\nNombre: ")
                    while nombre == "":
                        nombre = input("\nPor favor ingrese un nombre: ")
                    email = input("\nEmail: ")
                    while email == "":
                        email = input("\nPor favor ingrese un email: ")
                    telefono = input("\nTelefono: ")
                    while telefono == "":
                        telefono = input("\nPor favor ingrese un telefono: ")
                    direccion = input("\nDirección: ")
                    while direccion == "":
                        direccion = input("\nPor favor ingrese una direccion: ")
                    password = input("\nContraseña de ingreso para su cuenta: ")
                    while password == "" or len(password) < 5:
                        password = input("\nPor favor ingrese una contraseña valida de por lo menos 5 caracteres: ")


                    self.setNombre(nombre)
                    self.setEmail(email)
                    self.setTelefono(telefono)
                    self.setDireccion(direccion)

                    archivo = open("usuarios.txt","a")
                    archivo.write(usuario+";"+password+";"+nombre+";"+email+";"+telefono+";"+direccion+"\n")
                    archivo.close()

                    registro_terminado = 1

    def iniciar_sesion(lang):
        inicio_sesion_terminado = 0

        while inicio_sesion_terminado == 0:
            email = input(lang["email"])
            password = ""
            archivo = open("usuarios.txt","r")

            for linea in archivo:
                if linea.split(";")[0] == email:
                    password = input(lang["password"])

                    if password == linea.split(";")[1]:

                        return "Ha iniciado sesión con exito"
                        inicio_sesion_terminado = 1
                        archivo.close()
                        break
                    else:
                        return "Contraseña incorrecta, ingrese nuevamente sus datos."

            if password == "":

                return "No tenemos registro de su cuenta en nuestra base de datos. Por favor ingrese nuevamente su información"



# {
#     usuario_actual: Persona(...),
#     mensaje:
# }




