from Persona import Persona
from Producto import Producto
from Empleado import Empleado
from Mensajes import Mensajes
from Comentario import Comentario

class Main:
    usuario_actual = None
    personas = []
    productos = []
    empleados = []
    mensajes = None
    datos_ficticios_agregados = 0
    datos_ficticios_txt_agregados = 0
    breakOpciones = 0

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

        while Main.breakOpciones == 0:
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

                while Main.breakOpciones == 0:

                    opcionSeleccionada = int(input("\n-> "))

                    if opcionSeleccionada == 1:
                        Main.menuUsuariosLogReg()
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
    def menuUsuariosLogReg():
        print(Main.mensajes["client_login_menu"])

        while Main.breakOpciones == 0:
            opcionSeleccionada = int(input("\n-> "))

            if opcionSeleccionada == 1 or opcionSeleccionada == 2:
                Main.usuario_actual = Persona()
                operacion_completada = {}

                if opcionSeleccionada == 1:
                    email = input(Main.mensajes["email"])
                    password = input(Main.mensajes["user_password"])

                    Main.usuario_actual.setEmail(email)
                    Main.usuario_actual.setPassword(password)

                    operacion_completada = Main.usuario_actual.iniciar_sesion(Main.personas, Main.mensajes)

                elif opcionSeleccionada == 2:

                    nombre = input(Main.mensajes["user_name"])
                    email = input(Main.mensajes["email"])
                    telefono = input(Main.mensajes["user_phone"])
                    direccion = input(Main.mensajes["user_address"])
                    password = input(Main.mensajes["user_password"])

                    operacion_completada = Main.usuario_actual.registrarse(nombre, email, telefono, direccion, password,
                                                                           Main.personas,
                                                                           Main.mensajes)

                if operacion_completada["exitoso"] == True:
                    print(operacion_completada["mensaje"])
                    Main.menuUsuariosOpciones()

                else:
                    print(operacion_completada["mensaje"])
                    Main.menuUsuariosLogReg()

            elif opcionSeleccionada == 3:
                Main.menuPrincipal()

            else:
                print(Main.mensajes["wrong_option"])

    @staticmethod
    def menuUsuariosOpciones():

        print("\n" + Main.usuario_actual.getNombre() + Main.mensajes["client_menu"])

        while Main.breakOpciones == 0:
            opcionSeleccionada = int(input("\n-> "))

            if opcionSeleccionada == 1:
                if len(Main.productos) == 0:
                    print(Main.mensajes["product_not_found"])
                    input(Main.mensajes["go_back_press_any_key"])
                    Main.menuUsuariosOpciones()

                else:

                    for producto_actual in Main.productos:
                        print("------------------------------------------")
                        print(producto_actual.listarProductos(Main.mensajes))
                        print("------------------------------------------")

                    input(Main.mensajes["go_back_press_any_key"])
                    Main.menuUsuariosOpciones()


            elif opcionSeleccionada == 2:
                if len(Main.productos) == 0:

                    print(Main.mensajes["product_not_found"])
                    input(Main.mensajes["go_back_press_any_key"])
                    Main.menuUsuariosOpciones()

                else:
                    id_producto_buscar = int(input(Main.mensajes["insert_product_id"]))
                    info_produ_selec = Producto.seleccionarProducto(id_producto_buscar, Main.productos)

                    if info_produ_selec["encontrado"] == True:
                        print(Main.mensajes["select_product_menu"])
                        opcionSeleccionada = int(input("\n-> "))

                        if opcionSeleccionada == 1:
                            info_lista_deseos = Main.usuario_actual.agregar_lista_deseos(info_produ_selec["objeto"],
                                                                                         Main.mensajes)
                            print(info_lista_deseos["mensaje"])
                            input(Main.mensajes["go_back_press_any_key"])
                            Main.menuUsuariosOpciones()

                    else:
                        print(Main.mensajes["product_not_found"])
                        input(Main.mensajes["go_back_press_any_key"])
                        Main.menuUsuariosOpciones()


            elif opcionSeleccionada == 5:
                print(Main.mensajes["wish_list"])
                lista_deseos = Main.usuario_actual.getListaDeseos()
                for producto_actual in lista_deseos:
                    print("------------------------------------------")
                    print(producto_actual.listarProductos(Main.mensajes))
                    print("------------------------------------------")
                input(Main.mensajes["go_back_press_any_key"])
                Main.menuUsuariosOpciones()

            elif opcionSeleccionada == 7:
                Main.usuario_actual = None
                Main.menuPrincipal()

            else:
                print(Main.mensajes["wrong_option"])
                Main.menuUsuariosOpciones()

    @staticmethod
    def menuEmpleados():

        print(Main.mensajes["employee_login_menu"])

        while Main.breakOpciones == 0:
            opcionSeleccionada = int(input("\n-> "))

            if opcionSeleccionada == 1:
                Main.usuario_actual = Empleado()
                operacion_completada = {}

                email = input(Main.mensajes["email"])
                password = input(Main.mensajes["user_password"])

                Main.usuario_actual.setEmail(email)
                Main.usuario_actual.setPassword(password)

                operacion_completada = Main.usuario_actual.iniciar_sesion(Main.empleados, Main.mensajes)

                if operacion_completada["exitoso"] == True:
                    print(operacion_completada["mensaje"])
                    Main.menuEmpleadosOpciones()

                else:
                    print(operacion_completada["mensaje"])
                    Main.menuEmpleados()
            else:
                Main.menuPrincipal()

    @staticmethod
    def menuEmpleadosOpciones():
        print("\nBienvenid@ " + Main.usuario_actual.getNombre() + "\n" + Main.mensajes["employee_menu"])

        while Main.breakOpciones == 0:
            opcionSeleccionada = int(input("\n-> "))

            if opcionSeleccionada == 1 or opcionSeleccionada == 2:
                print(Main.mensajes["enter_data_employee"])

                nombre = input(Main.mensajes["user_name"])
                email = input(Main.mensajes["email"])
                password = input(Main.mensajes["user_password"])
                telefono = input(Main.mensajes["user_phone"])
                direccion = input(Main.mensajes["user_address"])
                admin = opcionSeleccionada == 1

                nuevo_empleado = Empleado(nombre, email, password, telefono, direccion, admin)
                print(nuevo_empleado.crearEmpleado(Main.empleados, Main.mensajes)["mensaje"])

            elif opcionSeleccionada == 5:

                print(Main.mensajes["enter_product_info"])
                nombre_producto = input(Main.mensajes["user_name"])
                valor_producto = float(input(Main.mensajes["value"]))
                descripcion_producto = input(Main.mensajes["description"])
                cantidad_inventario_producto = int(input(Main.mensajes["amount_inventory"]))

                producto = Producto(empleado=Main.usuario_actual, nombre=nombre_producto, valor=valor_producto,
                                    descripcion=descripcion_producto, cantidadInventario=cantidad_inventario_producto)
                print(producto.crearProducto(Main.productos, Main.mensajes))
                input(Main.mensajes["go_back_press_any_key"])
                Main.menuEmpleadosOpciones()


            elif opcionSeleccionada == 6:
                nombre_producto = input(print(Main.mensajes["product_to_search"]))
                lista_productos_buscados = Producto.buscarProductoNombre(nombre_producto, Main.productos)

                if len(lista_productos_buscados) > 0:
                    for producto_actual in lista_productos_buscados:
                        print("------------------------------------------")
                        print(producto_actual.listarProductos(Main.mensajes))
                        print("------------------------------------------")
                    input(Main.mensajes["go_back_press_any_key"])
                    Main.menuEmpleadosOpciones()
                else:
                    print(Main.mensajes["product_not_found"])
                    input(Main.mensajes["go_back_press_any_key"])
                    Main.menuEmpleadosOpciones()

            elif opcionSeleccionada == 7:
                id_producto_buscar = int(input(Main.mensajes["insert_product_id"]))
                info_produ_selec = Producto.seleccionarProducto(id_producto_buscar, Main.productos)

                if info_produ_selec["encontrado"] == True:

                    print(Main.mensajes["enter_product_info"])
                    nombre_producto = input(Main.mensajes["user_name"])
                    valor_producto = float(input(Main.mensajes["value"]))
                    descripcion_producto = input(Main.mensajes["description"])
                    cantidad_inventario_producto = int(input(Main.mensajes["amount_inventory"]))

                    info_produ_selec["objeto"].actualizarProducto(nombre_producto, valor_producto, descripcion_producto,
                                                                  cantidad_inventario_producto)
                    print(Main.mensajes["product_updated"])

                    input(Main.mensajes["go_back_press_any_key"])
                    Main.menuEmpleadosOpciones()

                else:

                    print(Main.mensajes["product_not_found"])
                    input(Main.mensajes["go_back_press_any_key"])
                    Main.menuEmpleadosOpciones()


            elif opcionSeleccionada == 8:
                id_producto_borrar = int(input(Main.mensajes["insert_product_id"]))
                print(Producto.borrarProducto(id_producto_borrar, Main.productos, Main.mensajes))
                input(Main.mensajes["go_back_press_any_key"])
                Main.menuEmpleadosOpciones()


            elif opcionSeleccionada == 11:
                Main.usuario_actual = None
                Main.menuPrincipal()

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
