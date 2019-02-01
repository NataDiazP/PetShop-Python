from Persona import Persona
from Producto import Producto
from Empleado import Empleado
from Mensajes import Mensajes


class Main:
    personas = []
    productos = []
    empleados = []
    mensajes = None
    datos_ficticios_agregados = 0
    datos_ficticios_txt_agregados = 0

    @staticmethod
    def setIdioma():

        print("""
			1. Español
			2. Inglés
		""")

        lang = int(input("\n-> "))

        if lang == 1:
            Main.mensajes = Mensajes.mensajes_es
        elif lang == 2:
            Main.mensajes = Mensajes.mensajes_eng

        Main.menuPrincipal()

    @staticmethod
    def menuPrincipal():

        print(Main.mensajes["welcome_menu"])
        breakOpciones = 0

        while breakOpciones == 0:
            opcionSeleccionada = int(input("\n-> "))
            if opcionSeleccionada == 1:
                if Main.datos_ficticios_agregados == 0:
                    Main.datosFicticios()
                    print(Main.mensajes["succes_dummy_data"])
                    Main.datos_ficticios_agregados = 1
                else:
                    print(Main.mensajes["dummy_data_added"])

                Main.menuPrincipal()

            elif opcionSeleccionada == 2:
                if Main.datos_ficticios_txt_agregados == 0:
                    Main.generarDatosFicticiosTxt()
                    print(Main.mensajes["succes_dummy_data"])
                    Main.datos_ficticios_txt_agregados = 1
                else:
                    print(Main.mensajes["dummy_data_added"])

                print(Main.datos_ficticios_txt_agregados)

                Main.menuPrincipal()
            elif opcionSeleccionada == 3:

                print(Main.mensajes["user_type"])

                while breakOpciones == 0:

                    opcionSeleccionada = int(input("\n-> "))

                    if opcionSeleccionada == 1:
                        Main.menuUsuarios()
                    elif opcionSeleccionada == 2:
                        Main.menuEmpleados()
                    elif opcionSeleccionada == 3:
                        Main.menuPrincipal()
                    else:
                        print(Main.mensajes["wrong_option"])

            elif opcionSeleccionada == 4:

                exit()

            else:

                print(Main.mensajes["wrong_option"])

    @staticmethod
    def menuUsuarios():
        print(Main.mensajes["client_login_menu"])
        breakOpciones = 0

        while breakOpciones == 0:
            opcionSeleccionada = int(input("\n-> "))

            if opcionSeleccionada == 1 or opcionSeleccionada == 2:
                usuario_actual = Persona()
                operacion_completada = {}

                if opcionSeleccionada == 1:
                    email = input(Main.mensajes["user_email"])
                    password = input(Main.mensajes["user_password"])

                    operacion_completada = usuario_actual.iniciar_sesion(email, password, Main.mensajes)

                elif opcionSeleccionada == 2:

                    nombre = input(Main.mensajes["user_name"])
                    email = input(Main.mensajes["user_email"])
                    telefono = input(Main.mensajes["user_phone"])
                    direccion = input(Main.mensajes["user_address"])
                    password = input(Main.mensajes["user_password"])

                    operacion_completada = usuario_actual.registrarse(nombre, email, telefono, direccion, password,
                                                                      Main.mensajes)

                if operacion_completada["exitoso"] == True:
                    print(operacion_completada["mensaje"])

                    print("\n" + usuario_actual.getNombre() + Main.mensajes["client_menu"])

                    while breakOpciones == 0:
                        opcionSeleccionada = int(input("\n-> "))

                        if opcionSeleccionada == 1:
                            for producto_actual in Main.productos:
                                print("------------------------------------------")
                                print(producto_actual.listarProductos())
                                print("------------------------------------------")

                else:
                    print(operacion_completada["mensaje"])
                    Main.menuUsuarios()

            elif opcionSeleccionada == 3:
                Main.menuPrincipal()

            else:
                print(Main.mensajes["wrong_option"])

    @staticmethod
    def menuEmpleados():

        print(Main.mensajes["employee_login_menu"])
        breakOpciones = 0

        while breakOpciones == 0:
            opcionSeleccionada = int(input("\n-> "))

            if opcionSeleccionada == 1:
                usuario_actual = Empleado()
                operacion_completada = {}

                email = input(Main.mensajes["user_email"])
                password = input(Main.mensajes["user_password"])

                usuario_actual.setEmail(email)
                usuario_actual.setPassword(password)

                operacion_completada = usuario_actual.iniciar_sesion(Main.empleados, Main.mensajes)

                if operacion_completada["exitoso"] == True:
                    print(operacion_completada["mensaje"])
                    usuario_actual = operacion_completada["datos"]

                    print("\n" + usuario_actual.getNombre() + Main.mensajes["employee_menu"])

                    while breakOpciones == 0:
                        opcionSeleccionada = int(input("\n-> "))

                        if opcionSeleccionada == 1:
                            print("hola")

                else:
                    print(operacion_completada["mensaje"])
                    Main.menuEmpleados()

    @staticmethod
    def generarDatosFicticiosTxt():
        archivo = open("empleados.txt", "r")

        for linea in archivo:
            datos = linea.split(";")

            empleado = Empleado(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6])
            Main.empleados.append(empleado)

        archivo.close()

    @staticmethod
    def datosFicticios():
        e1 = Empleado()
        p1 = Producto(empleado=e1, nombre="Collar para perro", valor=10000,
                      descripcion="Un bonito collar verde para perro")
        p2 = Producto(empleado=e1, nombre="Gimnasio para gato", valor=54000, descripcion="Una cosa de locos ")

        Main.productos.append(p1)
        Main.productos.append(p2)


if __name__ == "__main__":
    Main.setIdioma()
